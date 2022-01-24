import pathlib
from setuptools import setup

# The text of the README file
README = (pathlib.Path(__file__).parent / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="unmanic_api",
    version="0.0.1",
    description="An implementation of the Unmanic v2 API in Python.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/JeffResc/Unmanic-API",
    author="JeffResc",
    author_email="jeff@jeffresc.dev",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["unmanic_api"],
    include_package_data=True,
    install_requires=["urllib3==1.26.8"],
)