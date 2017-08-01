from distutils.core import setup

setup(
    author_email='keewynne90+github@gmail.com',
    author='Kieran Wynne',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.rst').read(),
    name='EuroMillions',
    packages=['euromillions',],
    url='https://github.com/k33k00/Euromillions-results',
    version='1.0',
    entry_points={
        'console_scripts': [
            'euromillions = euromillions.__init__:get_results',
        ],
    },
)
