from setuptools import setup

setup(
    name='warehouse',
    packages=['warehouse'],
    include_package_data=True,
    install_requires=[
        "numpy",
        "bson",
        "watchdog==0.9.0"
    ]
)