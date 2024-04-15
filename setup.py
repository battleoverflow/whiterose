###############################################
#                                             #
#   Whiterose Timing Library                  #
#   Author: battleoverflow                    #
#   GitHub: https://github.com/battleoverflow #
#                                             #
###############################################

import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "whiterose",
    version = "0.1.7",
    author = "battleoverflow",
    description = "Whiterose is a pure Python library built to return the current time in real-time within a single stdout. This Python library does not require any external libraries.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/battleoverflow/whiterose",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    py_modules=["whiterose"],
    python_requires = ">=3.6"
)
