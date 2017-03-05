sphinxcontrib-varlinks
======================

Provide support for substitutions in hyperlinks

Prerequisites
-------------

The following packages must be installed on your machine for this extension
to work:

-   python (>= 2.6).
-   python-sphinx (1.4.9 or later)

Replace ``python`` with ``python3`` if you plan to use the Python 3 version
of the extension.


Installation
------------

Installing this extension is done in just a few steps:

-   Download the latest version of the code from GitHub:
    https://github.com/fpoirotte/sphinxcontrib-varlinks/archive/master.tar.gz

-   Extract the contents of the archive and go into the newly created directory.

-   Then, install the extension from the machine's root account::

        root@localhost:~# # For Python 2
        root@localhost:~# python setup.py install
        root@localhost:~#
        root@localhost:~# # For Python 3
        root@localhost:~# python3 setup.py install

Please note that it is also possible to build a Debian package
for the extension (see below), which makes it easier to uninstall
the extension afterwards.


Debian package
--------------

If like me you prefer installing softwares from packages instead of sources
to ease maintenance, here's a quick guide on how to build a package for
this extension on Debian testing:

-   Make sure the dependencies are installed beforehand:

    ..  sourcecode:: bash

        clicky@me:~$ sudo apt-get install coreutils rename make tar dpkg-dev  debhelper dh-python \
            python-all python-setuptools python-sphinx python3-all python3-setuptools python3-sphinx

-   Download the latest version of the code from GitHub:
    https://github.com/fpoirotte/sphinxcontrib-varlinks/archive/master.tar.gz

-   Extract the tarball and go to the newly created directory.

-   Build the package by running::

        make deb

-   Run the following command to install the Python 2 module::

        sudo dpkg -i dist/python-sphinxcontrib.varlinks_*_all.deb

-   If you want to use the extension with Python 3, also run::

        sudo dpkg -i dist/python3-sphinxcontrib.varlinks_*_all.deb


Other .deb-based distributions and older Debian releases may require some
tweaking in the `packaging directory`__ for a package to be built correctly.

.. __: https://github.com/fpoirotte/sphinxcontrib-varlinks/blob/master/pkg/debian/


How to use
----------

Just load the extension in your ``conf.py``::

    extensions = [
        'sphinxcontrib.varlinks',
        # other extensions...
    ]

That's it! You may now use substitutions in hyperlinks like this:

..  sourcecode::

    This release can be downloaded `here <http://example.com/download#|release|>`_

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
