sphinxcontrib-varlinks
======================

Provide support for substitutions in hyperlinks

Installation
------------

Installing this extension is done in just a few steps:

-   Download the latest version of the code from GitHub:
    https://github.com/fpoirotte/sphinxcontrib-varlinks/archive/master.tar.gz

-   Extract the contents of the archive and go into the newly created directory.

-   Then, install the extension from the machine's root account::

        root@localhost:~# python setup.py install

Please note that it is also possible to build a Debian package
for the extension (see below), which makes it easier to uninstall
the extension afterwards.


Debian package
--------------

If like me you prefer installing softwares from packages instead of sources
to ease maintenance, here's a quick guide on how to build a package for
this extension on Debian testing:

-   Make sure the following packages are installed beforehand:

    -   debhelper
    -   python-all
    -   python-setuptools

-   Download the latest version of the code from GitHub:
    https://github.com/fpoirotte/sphinxcontrib-varlinks/archive/master.tar.gz

-   Rename the tarball into: ``sphinxcontrib-varlinks_<version>.orig.tar.gz``,
    where ``<version>`` matches the version string defined in `setup.py`__.

-   Extract the tarball and go to the newly created directory.

-   Build the package by running ``dpkg-buildpackage``.

-   Install the newly created package with
    ``sudo dpkg -i ../python-sphinxcontrib.varlinks_*_all.deb``

Other .deb-based distributions and older Debian releases may require some
tweaking in the `packaging directory`__ for a package to be built correctly.

.. __: https://github.com/fpoirotte/sphinxcontrib-varlinks/blob/master/setup.py
.. __: https://github.com/fpoirotte/sphinxcontrib-varlinks/blob/master/debian/


Prerequisites
-------------

The following packages must be installed on your machine for this extension
to work:

-   python (2.6.x or 2.7.x).
    The code has not been tested under Python 3.x.y yet.
-   python-sphinx (1.0.7 or later)


How to use
----------

Just load the extension in your ``conf.py``::

    extensions = [
        'sphinxcontrib.varlinks',
        # other extensions...
    ]

That's it! You may now use substitutions in hyperlinks like this:

..  sourcecode::

    This released can be downloaded `here <http://example.com/download#|release|>`_

Please note that you may use substitutions in both the hyperlink's label
and target.


Contributing
------------

-   `Fork the code on GitHub`__
-   Patch as necessary
-   Send a pull request

.. __: https://github.com/fpoirotte/sphinxcontrib-varlinks/fork


Bug reports
-----------

Bugs should be reported through the project's issue tracker on GitHub:
https://github.com/fpoirotte/sphinxcontrib-varlinks/issues.


License and credits
-------------------

This extension is licensed under the 2-clause BSD license.
See the `LICENSE`__ file for more information.

© 2017, François Poirotte <clicky@erebot.net>.

.. __: https://github.com/fpoirotte/sphinxcontrib-varlinks/blob/master/LICENSE
