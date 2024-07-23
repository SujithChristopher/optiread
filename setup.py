from setuptools import find_packages, setup

setup(
    name='optiread',
    packages=find_packages(include=['optiread']),
    version='0.1.0',
    description='My first Python library',
    author='Sujith Christopher',
    install_requires=['pandas', 'numpy', 'matplotlib', 'polars'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)