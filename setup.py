from distutils.core import setup

setup(
    author_email='keewynne90+github@gmail.com',
    author='Kieran Wynne',
    license='MIT',
    long_description=open('README.rst').read(),
    name='EuroMillions',
    packages=['euromillions'],
    url='https://github.com/k33k00/Euromillions-results',
    version='1.1.1',
    entry_points={
        'console_scripts': [
            'euromillions-all = Euromillions.euromillions:get_results',
            'euromillions-latest = Euromillions.euromillions:get_latest',
        ],
    },
)
