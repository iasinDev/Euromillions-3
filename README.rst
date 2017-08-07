================
EuroMillions results
================

.. image:: https://badge.fury.io/py/EuroMillions.svg
    :target: https://badge.fury.io/py/EuroMillions

Installation
------------
.. code-block:: bash

   $ pip install euromillions


Usage
-----

Python useage

.. code-block:: python

    >>> import euromillions
    >>> print(euromillions.get_results())
    >>> print(euromillions.get_latest)

Cli commands

.. code-block:: bash
    
    $ euromillions-latest
    {'draw_date': datetime.date(2017, 8, 4), 'balls':['29', '30', '36', '40', '41'], 'stars': ['2', '9'], 'miillionaire_maker': ['HNPB73135', 'MNNV98261'], 'draw_number': '1030'}
    
    $ euromillions-all
    [{'draw_date': datetime.date(2017, 8, 4), 'balls': ['29', '30', '36', '40', '41'], 'stars': ['2', '9'], 'miillionaire_maker': ['HNPB73135', 'MNNV98261'], 'draw_number': '1030'}, {'draw_date': datetime.date(2017, 8, 1), 'balls': ['14', '21', '24', '29', '30'], 'stars': ['8', '10'], 'miillionaire_maker': ['HLND68918', 'VLNF38111'], 'draw_number': '1029'}, ...]