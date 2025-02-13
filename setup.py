#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import io
from setuptools import setup

# Conditional dependency for futures
conditional_requirements = []
if sys.version_info < (3, 5):
    conditional_requirements.append('futures>=2.1.6')

# Read the contents of README file
with io.open('README.rst', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

# Read the contents of HISTORY file
with io.open('HISTORY.rst', 'r', encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

# Read the contents of requirements file and filter out 'http' based requirements
with io.open('requirements.txt', 'r', encoding='utf-8') as f:
    packages = set(f.read().splitlines())

requirements = list(filter(lambda x: "http" not in x, packages)) + conditional_requirements

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='polyglot',
    version='16.07.04',
    description='Polyglot is a natural language pipeline that supports massive multilingual applications.',
    long_description=readme + '\n\n' + history,
    author='Rami Al-Rfou',
    author_email='rmyeid@gmail.com',
    url='https://github.com/aboSamoor/polyglot',
    packages=[
        'polyglot',
        'polyglot.detect',
        'polyglot.tokenize',
        'polyglot.mapping',
        'polyglot.tag',
        'polyglot.transliteration',
    ],
    entry_points={
        'console_scripts': [
            'polyglot = polyglot.__main__:main',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3",
    zip_safe=False,
    keywords='polyglot',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: Afrikaans',
        'Natural Language :: Arabic',
        'Natural Language :: Bengali',
        'Natural Language :: Bosnian',
        'Natural Language :: Bulgarian',
        'Natural Language :: Catalan',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Natural Language :: Croatian',
        'Natural Language :: Czech',
        'Natural Language :: Danish',
        'Natural Language :: Dutch',
        'Natural Language :: English',
        'Natural Language :: Esperanto',
        'Natural Language :: Finnish',
        'Natural Language :: French',
        'Natural Language :: Galician',
        'Natural Language :: German',
        'Natural Language :: Greek',
        'Natural Language :: Hebrew',
        'Natural Language :: Hindi',
        'Natural Language :: Hungarian',
        'Natural Language :: Icelandic',
        'Natural Language :: Indonesian',
        'Natural Language :: Italian',
        'Natural Language :: Japanese',
        'Natural Language :: Javanese',
        'Natural Language :: Korean',
        'Natural Language :: Latin',
        'Natural Language :: Latvian',
        'Natural Language :: Macedonian',
        'Natural Language :: Malay',
        'Natural Language :: Marathi',
        'Natural Language :: Norwegian',
        'Natural Language :: Panjabi',
        'Natural Language :: Persian',
        'Natural Language :: Polish',
        'Natural Language :: Portuguese',
        'Natural Language :: Portuguese (Brazilian)',
        'Natural Language :: Romanian',
        'Natural Language :: Russian',
        'Natural Language :: Serbian',
        'Natural Language :: Slovak',
        'Natural Language :: Slovenian',
        'Natural Language :: Spanish',
        'Natural Language :: Swedish',
        'Natural Language :: Tamil',
        'Natural Language :: Telugu',
        'Natural Language :: Thai',
        'Natural Language :: Turkish',
        'Natural Language :: Ukranian',
        'Natural Language :: Urdu',
        'Natural Language :: Vietnamese',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Linguistic',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
