from setuptools import find_packages, setup

# PyPI only supports nicely-formatted README files in reStructuredText.
# Newsapps seems to prefer Markdown.  Use a version of the pattern from
# https://coderwall.com/p/qawuyq/use-markdown-readme-s-in-python-modules
# to convert the Markdown README to rst if the pypandoc package is
# present.
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, OSError):
    long_description = open('README.md').read()

# Load the version from the version module
exec(open('slackunfuddle/version.py').read())

setup(
    name='slackunfuddle',
    version=__version__,
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        'Flask',
        'requests',
        'lxml',
    ],
    tests_require=[
        'nose',
    ],
    test_suite='nose.collector',
)
