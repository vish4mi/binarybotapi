"""The python wrapper for Binary Option API package setup."""
with open("README.md", "r") as fh:
    long_description = fh.read()

import setuptools

setuptools.setup(
    name="binarybotapi",
    version="0.0.5",
    author="Vishal Bhadade",
    author_email="vishal.bhadade@gmail.com",
    description="Binary Option API for IQOption in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vish4mi/binarybotapi",
    packages=setuptools.find_packages(),
    install_requires=["pylint","requests","websocket-client"],
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    zip_safe=False
)
