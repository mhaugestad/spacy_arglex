#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spacy_arglex", # Replace with your own username
    version="0.0.1",
    author="Mathias Haugestad",
    author_email="mhaugestad@gmail.com",
    description="Package to detect opinion phrases built on top of spacy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mhaugestad/spacy_arglex",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["spacy","spacy-models @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz"],
    python_requires='>=3.6',
)
