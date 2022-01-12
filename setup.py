"""
    HighCohesion API

    HighCohesion API [https://highcohesion.co.uk](https://highcohesion.co.uk)   # noqa: E501

    The version of the OpenAPI document: 1.0.21
    Contact: admin@highcohesion.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "openapi-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="HighCohesion API",
    author="OpenAPI Generator community",
    author_email="admin@highcohesion.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "HighCohesion API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    HighCohesion API [https://highcohesion.co.uk](https://highcohesion.co.uk)   # noqa: E501
    """
)