================
EuroMillions results
================

.. image:: https://img.shields.io/codacy/grade/437f61de022b44fda7779442c700811b.svg
    :target: https://www.codacy.com/app/k33k00/Euromillions?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=k33k00/Euromillions&amp;utm_campaign=Badge_Grade
    
.. image:: https://img.shields.io/codacy/coverage/437f61de022b44fda7779442c700811b.svg
   :target: https://www.codacy.com/app/k33k00/Euromillions?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=k33k00/Euromillions&amp;utm_campaign=Badge_Coverage#

.. image:: https://badge.fury.io/py/EuroMillions.svg
    :target: https://badge.fury.io/py/EuroMillions
    
.. image:: https://img.shields.io/pypi/pyversions/EuroMillions.svg
    :target: 

.. image:: https://img.shields.io/pypi/l/EuroMillions.svg
   :target: 

Installation
------------
.. code-block:: bash

   $ pip install euromillions


Usage
-----

Python useage

.. code-block:: python

    from euromillions.euromillions import Euromillions
    e = Euromillions()
    print(e.get_latest_draw())
    print(e.get_results())