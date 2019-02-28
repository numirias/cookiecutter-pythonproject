{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}
from os import path
import sys

from setuptools import setup, find_packages


# Open encoding isn't available for Python 2.7 (sigh)
if sys.version_info < (3, 0):
    from io import open

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest-runner',{%- endif %}]
test_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest',{%- endif %}]

setup(
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.email }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
{%- if cookiecutter.license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description='{{ cookiecutter.project_short_description }}',
    {%- if cookiecutter.cli %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.package_name }}={{ cookiecutter.package_name }}.cli:main',
        ],
    },
    {%- endif %}
    install_requires=[],
{%- if cookiecutter.license in license_classifiers %}
    license='{{ cookiecutter.license }}',
{%- endif %}
    long_description=long_description,
    long_description_content_type='text/markdown',
    # Include data files specified in MANIFEST.in
    include_package_data=True,
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages(where='src'),
    package_dir={'':'src'},
    setup_requires=setup_requirements,
    # TODO Needed?
    test_suite='test',
    # TODO Needed?
    tests_require=test_requirements,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
)
