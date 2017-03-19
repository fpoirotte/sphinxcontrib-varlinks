# -*- coding: utf-8 -*-
"""
    Variable hyperlinks
    ~~~~~~~~~~~~~~~~~~~

    Extension that adds support for substitutions in hyperlinks.
    Substitutions are supported in both the link's label
    and target.

    Eg. `Download |subproject| <http://example.com/|subproject|/>`_.

    :copyright: Copyright 2017 by Francois Poirotte.
    :license: BSD, see LICENSE for details.
"""
import re
from docutils import nodes
from docutils.transforms import Transform

__all__ = ['setup']

__version__ = '0.1.2'


class LinkSubstitutionTransform(Transform):
    subst_pattern = r'\|([^|]+)\|'

    def _maybe_hyperlink(self, node):
        return isinstance(node, (nodes.reference, nodes.target))


class LinkSubstitutionPhase1(LinkSubstitutionTransform):
    # This transformation is applied very early.
    # At a minimum, it must be run before substitutions are applied.
    default_priority = 10

    def apply(self):
        """Create substitution nodes for hyperlinks"""
        # In this phase, we look for hyperlinks (references nodes)
        # that contain substitutions (of the form "|foo|").
        # We then add actual "substitution"s nodes to those references,
        # so that they can be replaced by the substitution processor.
        subst_re = re.compile(self.subst_pattern)

        for link in self.document.traverse(self._maybe_hyperlink):
            if 'refuri' not in link:
                continue

            # Note: "target" nodes do not have a "name" attribute.
            if '|' not in link['refuri'] and '|' not in link.get('name', ''):
                continue

            # This list acts as a cache so that only one substitution node
            # is added as a child for each substitution name.
            substitutions = []

            matches = subst_re.findall(link['refuri']) + \
                subst_re.findall(link.get('name', ''))
            for subref_text in matches:
                if subref_text in substitutions:
                    continue

                substitutions.append(subref_text)
                subref_node = nodes.substitution_reference(subref_text)
                link.append(subref_node)
                self.document.note_substitution_ref(subref_node, subref_text)

            # Build a map of substitutions names to child indices
            # (minus one since the actual link label is in link[0]).
            link['varlinks'] = \
                dict(zip(substitutions, range(len(substitutions))))


class LinkSubstitutionPhase2(LinkSubstitutionTransform):
    # Apply this transformation right after substitutions have been applied.
    default_priority = 221

    def _replace(self, mapping, sub, offset):
        def inner(match):
            name = match.group()
            return sub[mapping[name[1:-1]] + offset]
        return inner

    def apply(self):
        """Replace substitutions in hyperlinks with their contents"""
        # In this phase, we replace the substitutions in hyperlinks
        # with the contents of the sub-nodes introduced during phase 1.
        # We also remove those temporary nodes from the tree.
        subst_re = re.compile(self.subst_pattern)

        # Apply the substitutions to hyperlink references.
        for link in self.document.traverse(nodes.reference):
            substitutions = link.get('varlinks')
            if not substitutions:
                continue

            replacer = self._replace(substitutions, link.children, 1)
            link['refuri'] = subst_re.sub(replacer, link['refuri'])
            content = subst_re.sub(replacer, link[0])
            # Cleanup the temporary nodes and recreate the node's content.
            link.clear()
            del link['varlinks']
            link.append(nodes.Text(content))

        # Do the same with hyperlink targets.
        for link in self.document.traverse(nodes.target):
            substitutions = link.get('varlinks')
            if not substitutions:
                continue

            replacer = self._replace(substitutions, link.children, 0)
            link['refuri'] = subst_re.sub(replacer, link['refuri'])
            # Cleanup the temporary nodes.
            link.clear()
            del link['varlinks']


def setup(app):
    app.add_transform(LinkSubstitutionPhase1)
    app.add_transform(LinkSubstitutionPhase2)
