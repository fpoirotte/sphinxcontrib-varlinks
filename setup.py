# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from sphinxcontrib import varlinks

long_desc = '''
sphinxcontrib.varlinks is an extension for Sphinx that makes it
possible to use substitutions in hyperlinks, thus enabling the use
of variable links.
'''

setup(
    name='sphinxcontrib-varlinks',
    version=varlinks.__version__,
    url='https://github.com/fpoirotte/sphinxcontrib-varlinks',
    download_url='https://github.com/fpoirotte/sphinxcontrib-varlinks',
    license='BSD',
    author='Francois Poirotte',
    author_email='clicky@erebot.net',
    description='Support substitutions in Sphinx hyperlinks',
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
        'Sphinx>=1.3.6',
        'Sphinx<=1.6',
    ],
    test_suite='nose.collector',
    namespace_packages=['sphinxcontrib'],
)
