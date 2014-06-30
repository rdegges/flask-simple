"""
flask-simple
~~~~~~~~~~~~

SimpleDB integration for Flask!

Please visit this project's GitHub page to view all docs:
https://github.com/rdegges/flask-simple

-Randall
"""


from subprocess import call

from setuptools import Command, setup

from flask_dynamo import __version__ as version


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test'])
        raise SystemExit(errno)


setup(

    # Basic package information:
    name = 'flask-simple',
    version = version,
    packages = ['flask_simple'],

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['boto>=2.29.1', 'Flask>=0.10.1'],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'r@rdegges.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/flask-simple',
    keywords = 'python simpledb dynamo aws amazon flask web database',
    description = 'SimpleDB integration for Flask.',
    long_description = __doc__,

    # Classifiers:
    platforms = 'any',
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Database',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    # Test helper:
    cmdclass = {'test': RunTests},

)
