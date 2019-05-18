Testing macaddress
==================

To conduct testing, run the following commands from your shell.

.. code-block:: console

   [user@host macaddress]$ flake8 --count --ignore E125 macaddress
   [user@host macaddress]$ pytest --cov --cov-report=term-missing
