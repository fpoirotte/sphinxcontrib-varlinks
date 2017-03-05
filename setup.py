# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

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
    description='Use substitutions in Sphinx hyperlinks',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
    ],
    keywords="sphinx hyperlinks substitutions",
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Sphinx>=1.4.9',
    ],
    test_suite='nose.collector',
    namespace_packages=['sphinxcontrib'],
)
