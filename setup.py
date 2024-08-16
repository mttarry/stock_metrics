from setuptools import setup, find_packages

setup(
    name='stock_metrics',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'yfinance',
        'matplotlib'
    ],
    description='A library for calculating stock metrics.',
    author='Matt Tarry',    
)