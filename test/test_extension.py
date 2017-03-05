"""
    test_embedded
    ~~~~~~~~~~~~~

    Test that embedded URIs work.
"""

import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from os.path import join
from sphinx_testing.util import path, with_app


class TestExtension(unittest.TestCase):
    def test_embedded(self):
        @with_app(buildername='html', srcdir=path(__file__).dirname() / 'embedded', warningiserror=True)
        def execute(app, status, warning):
            app.build()
            self.assertIn('<a class="reference external" href="http://example.com/download#v1.2.3">Download version 1.2.3</a>',
                          (app.outdir / 'contents.html').read_text())

        execute()

