# coding: utf-8

"""
    IGVF Project API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 52.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "igvf-client"
VERSION = "52.0.2"
PYTHON_REQUIRES = ">=3.9"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="IGVF Project API",
    author="IGVF DACC",
    author_email="encode-help@lists.stanford.edu",
    url="https://github.com/iGVF-DACC/igvf-python-client",
    keywords=["OpenAPI", "OpenAPI-Generator", "IGVF Project API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    Autogenerated Python client for the IGVF API
    """,  # noqa: E501
    package_data={"igvf_client": ["py.typed"]},
)
