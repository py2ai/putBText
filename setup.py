import pathlib
from setuptools import setup
# from distutils.core import setup
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pyshine",
    version="0.0.4",
    description="This library contains various Audio and Video Signal Processing utilities",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/py2ai/audioCapture",
    author="PyShine",
    author_email="python2ai@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["pyshine"],
    include_package_data=True,
    install_requires=['numpy','sounddevice'],
    entry_points={
        "console_scripts": [

        ]
    },
)
