import os
from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    author_email='keewynne90+github@gmail.com',
    author='Kieran Wynne',
    license='MIT',
    long_description=readme(),
    name='EuroMillions',
    packages=['euromillions'],
    url='https://github.com/k33k00/Euromillions-results',
    version='2.1.4',
    entry_points={
        'console_scripts': [
            'euromillions-all = Euromillions.euromillions:get_results',
            'euromillions-latest = Euromillions.euromillions:get_latest',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
