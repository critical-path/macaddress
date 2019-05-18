Installing macaddress
=====================

macaddress is available on GitHub at https://github.com/critical-path/macaddress.

If your version of pip is >= 18.1:
----------------------------------

To install macaddress with test-related dependencies, run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install --editable git+https://github.com/critical-path/macaddress.git#egg=macaddress[test]

To install it without test-related dependencies, run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install git+https://github.com/critical-path/macaddress.git

If your version of pip is < 18.1:
---------------------------------

To install macaddress with test-related dependencies, run the following commands from your shell.

.. code-block:: console

   [user@host ~]$ git clone git@github.com:critical-path/macaddress.git
   [user@host ~]$ cd macaddress
   [user@host macaddress]$ sudo pip install --editable .[test]

To install it without test-related dependencies, run the following commands from your shell.

.. code-block:: console

   [user@host ~]$ git clone git@github.com:critical-path/macaddress.git
   [user@host ~]$ cd macaddress
   [user@host macaddress]$ sudo pip install .

(If necessary, replace :code:`pip` with :code:`pip3`.)
