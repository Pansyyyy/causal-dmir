import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 6):
    sys.exit("Sorry, Python < 3.6 is not supported.")

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="causal-dmir",
    version="0.0.1",
    description="A pip package",
    license="GPL",
    author="DMIRLab",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scipy>=1.7.3',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Operating System :: OS Independent',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires='>=3.6',
)