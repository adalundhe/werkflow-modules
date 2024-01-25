import os
from setuptools import (
    setup,
    find_packages
)

current_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(current_directory, 'README.md'), "r") as readme:
    package_description = readme.read()

version_string = ""
with open (os.path.join(current_directory, ".version"), 'r') as version_file:
    version_string = version_file.read()

setup(
    name="werkflow-github",
    version=version_string,
    description="A Github module for Werkflow.",
    long_description=package_description,
    long_description_content_type="text/markdown",
    author="Ada Lundhe",
    author_email="corpheus91@gmail.com.com",
    url="https://github.com/scorbettUM/werkflow-modules/werkflow-github",
    packages=find_packages(),
    keywords=[
        'pypi', 
        'cicd', 
        'python',
        'setup',
        'repo',
        'project',
        'migrate',
        'monorepo',
        'github'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'werkflow',
        'werkflow-encryption',
        'werkflow-http'
    ],
    python_requires='>=3.8'
)
