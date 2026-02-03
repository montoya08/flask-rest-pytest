from setuptools import setup, find_packages

setup(
    name="flask_rest_pytest",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "pytest",
        "requests"
    ],
)
