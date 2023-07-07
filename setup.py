import os
from setuptools import setup, find_packages

version = None
author = None

with open(os.path.join("threadspy", "__init__.py"), encoding="utf-8") as f:
    for line in f:
        if line.strip().startswith("__version__"):
            version = line.split("=")[1].strip().replace('"', "").replace("'", "")
        if line.strip().startswith("__author__"):
            author = line.split("=")[1].strip().replace('"', "").replace("'", "")

setup(
    name="threads-py",
    version=version,
    author=author,
    author_email="i@junho.io",
    url="https://github.com/junhoyeo/threads-py",
    license="MIT License",
    description="Unofficial, Reverse-Engineered Python client for Meta's Threads.",
    long_description_content_type="text/markdown",
    platforms=["any"],
    packages=find_packages(exclude=["tests", "assets"]),
    install_requires=["requests", "dataclasses", "dataclasses-json"],
    python_requires=">=3.8",
)
