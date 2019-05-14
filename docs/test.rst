Testing macaddress
==================

To conduct static tests, run the following command from your shell.

.. code-block:: console

   [user@host macaddress]$ flake8 --count --ignore E125 macaddress

To conduct dynamic (unit) tests, run the following command from your shell.

.. code-block:: console

   [user@host macaddress]$ pytest --cov --cov-report=term-missing
