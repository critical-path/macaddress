.. image:: https://travis-ci.com/critical-path/macaddress.svg?branch=master
   :target: https://travis-ci.com/critical-path/macaddress
    
.. image:: https://coveralls.io/repos/github/critical-path/macaddress/badge.svg?branch=master
   :target: https://coveralls.io/github/critical-path/macaddress?branch=master

.. image:: https://readthedocs.org/projects/macaddress/badge/?version=latest
   :target: https://macaddress.readthedocs.io/en/latest/?badge=latest

Introduction
============

Media access control (MAC) addresses play an important role in local-area networks.  They also pack a lot of information into 48-bit hexadecimal strings!

The macaddress library makes it easy to evaluate the properties of MAC addresses and the `extended identifiers <https://standards.ieee.org/products-services/regauth/tut/index.html>`__ of which they are subclasses.


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

(If necessary, replace :code:`pip` with :code:`pip3` in any of the scenarios above.)


Using macaddress
================

While macaddress contains multiple classes, the only one with which you need to interact directly is :code:`MediaAccessControlAddress`.

Import :code:`MediaAccessControlAddress`.

.. code-block:: python

   >>> from macaddress import MediaAccessControlAddress

Instantiate :code:`MediaAccessControlAddress` by passing in a MAC address in plain, hyphen, colon, or dot notation.

.. code-block:: python

   >>> mac = MediaAccessControlAddress("a0b1c2d3e4f5")

.. code-block:: python

   >>> mac = MediaAccessControlAddress("a0-b1-c2-d3-e4-f5")

.. code-block:: python

   >>> mac = MediaAccessControlAddress("a0:b1:c2:d3:e4:f5")

.. code-block:: python

   >>> mac = MediaAccessControlAddress("a0b1.c2d3.e4f5")

To determine whether the MAC address is a broadcast, a multicast (layer-two), or a unicast address, access its :code:`is_broadcast`, :code:`is_multicast`, and :code:`is_unicast` properties.

.. code-block:: python

   >>> print(mac.is_broadcast)
   False

.. code-block:: python

   >>> print(mac.is_multicast)
   False

.. code-block:: python

   >>> print(mac.is_unicast)
   True

To determine whether the MAC address is a universally-administered address (UAA) or a locally-administered address (LAA), access its :code:`is_uaa` and :code:`is_laa` properties.

.. code-block:: python

   >>> print(mac.is_uaa)
   True

.. code-block:: python

   >>> print(mac.is_laa)
   False

To work with the MAC address's octets, access its :code:`octets` property, which contains six :code:`Octet` objects.

.. code-block:: python

   >>> print(mac.octets) 
   [Octet('a0'), Octet('b1'), Octet('c2'), Octet('d3'), Octet('e4'), Octet('f5')]

To determine whether the MAC address is an extended unique identifier (EUI), an extended local identifier (ELI), or unknown, access its :code:`type` property.

.. code-block:: python

   >>> print(mac.type)
   unique

To determine whether the MAC address has an organizationally-unique identifier (OUI) or a company ID (CID), access its :code:`has_oui` and :code:`has_cid` properties.

.. code-block:: python

   >>> print(mac.has_oui)
   True

.. code-block:: python

   >>> print(mac.has_cid)
   False

To view the binary equivalent of the MAC address, access its :code:`binary` and :code:`reverse_binary` properties.  With :code:`binary`, the most-significant digit of each octet appears first.  With :code:`reverse_binary`, the least-significant digit of each octet appears first.

.. code-block:: python

   >>> print(mac.binary)
   101000001011000111000010110100111110010011110101

.. code-block:: python

   >>> print(mac.reverse_binary)
   000001011000110101000011110010110010011110101111

To return the MAC address's two "fragments," call the :code:`to_fragments` method.  For an EUI, this means the 24-bit OUI as the first fragment and the remaining interface-specific bits as the second fragment.  For an ELI, this means the 24-bit CID as the first fragment and the remaining interface-specific bits as the second fragment.

.. code-block:: python

   >>> fragments = mac.to_fragments()
   >>> print(fragments)
   ('a0b1c2', 'd3e4f5')

To return the MAC address in different notations, call the :code:`to_plain_notation`, :code:`to_hyphen_notation`, :code:`to_colon_notation`, and :code:`to_dot_notation` methods.

.. code-block:: python

   >>> plain = mac.to_plain_notation()
   >>> print(plain)
   a0b1c2d3e4f5

.. code-block:: python

   >>> hyphen = mac.to_hyphen_notation()
   >>> print(hyphen)
   a0-b1-c2-d3-e4-f5

.. code-block:: python

   >>> colon = mac.to_colon_notation()
   >>> print(colon)
   a0:b1:c2:d3:e4:f5

.. code-block:: python

   >>> dot = mac.to_dot_notation()
   >>> print(dot)
   a0b1.c2d3.e4f5


Testing macaddress
==================

To conduct static tests, run the following command from your shell.

.. code-block:: console

   [user@host macaddress]$ flake8 --count --ignore E125 macaddress

To conduct dynamic (unit) tests, run the following command from your shell.

.. code-block:: console

   [user@host macaddress]$ pytest --cov --cov-report=term-missing
