from distutils.core import setup

setup(
    author_email='keewynne90+github@gmail.com',
    author='Kieran Wynne',
    license='MIT',
    long_description=open('README.rst').read(),
    name='EuroMillions',
    packages=['euromillions'],
    url='https://github.com/k33k00/Euromillions-results',
    version='2.1.1',
    entry_points={
        'console_scripts': [
            'euromillions-all = Euromillions.euromillions:get_results',
            'euromillions-latest = Euromillions.euromillions:get_latest',
        ],
    },
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ],
)
