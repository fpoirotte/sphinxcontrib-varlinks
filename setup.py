# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

import os
import sys

long_desc = '''
sphinxcontrib.varlinks is an extension for Sphinx that makes it
possible to use substitutions in hyperlinks, thus enabling the use
of variable links.
'''

setup(
    name='sphinxcontrib-varlinks',
    version='0.1.0',
    url='https://github.com/fpoirotte/sphinxcontrib-varlinks',
    download_url='https://github.com/fpoirotte/sphinxcontrib-varlinks',
    license='BSD',
    author='Francois Poirotte',
    author_email='clicky@erebot.net',
    description='Support for substitutions in hyperlinks',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Documentation',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Sphinx>=1.0.7',
    ],
    use_2to3=True,
)
