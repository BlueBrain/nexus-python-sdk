__author__ = "Pierre-Alexandre Fonta"
__maintainer__ = "Pierre-Alexandre Fonta"

import os

from setuptools import setup

VERSION = "0.1.0"

HERE = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file.
with open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="nexus-sdk",
    version=VERSION,
    description="Python SDK for Blue Brain Nexus v1.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="nexus sdk",
    url="https://github.com/BlueBrain/nexus-python-sdk",
    author="Pierre-Alexandre Fonta, Jonathan Lurie",
    author_email=", pierre-alexandre.fonta@epfl.ch, jonathan.lurie@epfl.ch",
    license="Apache License, Version 2.0",
    packages=["nexussdk"],
    python_requires=">=3.5",
    install_requires=[
        "requests",
    ],
    extras_require={
        "test": ["pytest", "pytest-cov"],
    },
    data_files=[("", ["LICENSE.txt"])],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "Topic :: Database",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5'",
        "Programming Language :: Python :: 3.6'",
        "Programming Language :: Python :: 3.7'",
        "Programming Language :: Python :: 3.8'",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Natural Language :: English",
    ]
)
