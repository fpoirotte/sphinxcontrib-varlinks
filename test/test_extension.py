"""
    test_embedded
    ~~~~~~~~~~~~~

    Test that embedded URIs work.
"""

import sys
from sphinx_testing.util import path, with_app
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class TestExtension(unittest.TestCase):
    def test_embedded(self):
        srcdir = path(__file__).dirname() / 'embedded'

        @with_app(buildername='html', srcdir=srcdir, warningiserror=True)
        def execute(app, status, warning):
            app.build()
            # Explicit embedded URL with a label
            res = '<a class="reference external" ' \
                  'href="http://example.com/download#v1.2.3">'\
                  'Download version 1.2.3</a>'
            self.assertIn(res, (app.outdir / 'contents.html').read_text())

            # Explicit embedded URL without any label
            res = '<a class="reference external" ' \
                  'href="http://example.com/changelog#v1.2.3">'\
                  'http://example.com/changelog#v1.2.3</a>'
            self.assertIn(res, (app.outdir / 'contents.html').read_text())

        execute()

    def test_indirect(self):
        srcdir = path(__file__).dirname() / 'indirect'

        @with_app(buildername='html', srcdir=srcdir, warningiserror=True)
        def execute(app, status, warning):
            app.build()
            varlink = 'https://docs.python.org/3.4/whatsnew/changelog.html'
            res = '<p><a class="reference external" href="%s">Python</a> is ' \
                  'a <a class="reference external" href="%s">cool ' \
                  'language</a>.</p>\n' % (varlink, varlink)
            self.assertIn(res, (app.outdir / 'contents.html').read_text())

        execute()
