"""The python wrapper for Binary Option API package setup."""
from setuptools import (setup, find_packages)


setup(
    name="binarybotapi",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["pylint","requests","websocket-client"],
    include_package_data = True,
    description="Binary Option API for IQOption in python",
    long_description="Binary Option API for IQOption in python",
    url="https://github.com/vish4mi/binarybotapi",
    author="Vishal Bhadade",
    author_email="vishal.bhadade@gmail.com",
    zip_safe=False
)
