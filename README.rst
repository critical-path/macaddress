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

If you do not have pip version 18.1 or higher, then run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install --upgrade pip

To install macaddress with test-related dependencies, run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install --editable git+https://github.com/critical-path/macaddress.git#egg=macaddress[test]

To install it without test-related dependencies, run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install git+https://github.com/critical-path/macaddress.git

(If necessary, replace :code:`pip` with :code:`pip3`.)


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

To view the decimal equivalent of the MAC address, access its :code:`decimal` property.

.. code-block:: python

   >>> print(mac.decimal)
   176685338322165

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


Patterns for macaddress
=======================

Create a range of MAC addresses
-------------------------------

.. code-block:: python

   # Import `pprint.pprint` and `macaddress.MediaAccessControlAddress`.

   >>> from pprint import pprint
   >>> from macaddress import MediaAccessControlAddress

   # Identify the start and end of the range.

   >>> start_mac = MediaAccessControlAddress("a0b1c2d3e4f5")
   >>> end_mac = MediaAccessControlAddress("a0b1c2d3e4ff")

   # Create a list containing one `MediaAccessControlAddress` object 
   # for each address in the range.

   >>> mac_range = [
   ...   MediaAccessControlAddress(format(decimal, "x"))
   ...   for decimal in range(start_mac.decimal, end_mac.decimal + 1)
   ... ]

   # Do something useful with the results, such as returning
   # the colon notation of each MAC address in the list.

   >>> colons = [
   ...     mac.to_colon_notation() for mac in mac_range
   ... ]
   >>> pprint(colons)
   ["a0:b1:c2:d3:e4:f5", 
    "a0:b1:c2:d3:e4:f6", 
    "a0:b1:c2:d3:e4:f7", 
    "a0:b1:c2:d3:e4:f8", 
    "a0:b1:c2:d3:e4:f9", 
    "a0:b1:c2:d3:e4:fa", 
    "a0:b1:c2:d3:e4:fb", 
    "a0:b1:c2:d3:e4:fc", 
    "a0:b1:c2:d3:e4:fd", 
    "a0:b1:c2:d3:e4:fe", 
    "a0:b1:c2:d3:e4:ff"]

Map-reduce a list of MAC addresses
----------------------------------

.. code-block:: python

   # Import `functools.reduce`, `pprint.pprint`, and 
   # `macaddress.MediaAccessControlAddress`.

   >>> from functools import reduce
   >>> from pprint import pprint
   >>> from macaddress import MediaAccessControlAddress

   # Define `transform`, which is our map function.

   >>> def transform(mac, attributes):
   ...     transformed = {}
   ...     transformed[mac.normalized] = {}
   ...     for attribute in attributes:
   ...         transformed[mac.normalized][attribute] = getattr(mac, attribute)
   ...     return transformed
   ...

   # Define `fold`, which is our reduce function.

   >>> def fold(current_mac, next_mac):
   ...     for key, value in next_mac.items():
   ...         if key in current_mac:
   ...             pass
   ...         else:
   ...             current_mac[key] = value
   ...     return current_mac
   ...

   # Define `map_reduce`, which calls `functools.reduce`, `transform`, and `fold`.

   >>> def map_reduce(macs, attributes):
   ...     return reduce(fold, [transform(mac, attributes) for mac in macs])
   ...

   # Identify addresses of interest.

   >>> addresses = [
   ...     "a0:b1:c2:d3:e4:f5", 
   ...     "a0:b1:c2:d3:e4:f6", 
   ...     "a0:b1:c2:d3:e4:f7", 
   ...     "a0:b1:c2:d3:e4:f8", 
   ...     "a0:b1:c2:d3:e4:f9", 
   ...     "a0:b1:c2:d3:e4:fa", 
   ...     "a0:b1:c2:d3:e4:fb", 
   ...     "a0:b1:c2:d3:e4:fc", 
   ...     "a0:b1:c2:d3:e4:fd", 
   ...     "a0:b1:c2:d3:e4:fe", 
   ...     "a0:b1:c2:d3:e4:ff"
   ... ]

   # Create a list containing one `MediaAccessControlAddress` object
   # for each address of interest.

   >>> macs = [
   ...     MediaAccessControlAddress(address) for address in addresses
   ... ]

   # Create a list with attributes of interest.

   >>> attributes = [
   ...     "is_unicast", 
   ...     "is_uaa"
   ... ]

   # Call `map_reduce`, passing in the lists of `MediaAccessControlAddress`
   # objects and attributes.

   >>> mapped_reduced = map_reduce(macs, attributes)
   >>> pprint(mapped_reduced)
   {"a0b1c2d3e4f5": {"is_uaa": True, "is_unicast": True},
    "a0b1c2d3e4f6": {"is_uaa": True, "is_unicast": True},
    "a0b1c2d3e4f7": {"is_uaa": True, "is_unicast": True},
    "a0b1c2d3e4f8": {"is_uaa": True, "is_unicast": True},
    "a0b1c2d3e4f9": {"is_uaa": True, "is_unicast": True},
    "a0b1c2d3e4fa": {"is_uaa": True, "is_unicast": True},
    "a0b1c2d3e4fb": {"is_uaa": True, "is_unicast": True},
    "a0b1c2d3e4fc": {"is_uaa": True, "is_unicast": True},
    "a0b1c2d3e4fd": {"is_uaa": True, "is_unicast": True},
    "a0b1c2d3e4fe": {"is_uaa": True, "is_unicast": True},
    "a0b1c2d3e4ff": {"is_uaa": True, "is_unicast": True}}

Serialize the attributes of a MAC address
-----------------------------------------

.. code-block:: python

   # Import `json.dumps`.

   >>> from json import dumps

   # Identify the addresses and attributes of interest.

   >>> unserialized = {
   ...     "a0b1c2d3e4f5": {"is_uaa": True, "is_unicast": True},
   ...     "a0b1c2d3e4f6": {"is_uaa": True, "is_unicast": True},
   ...     "a0b1c2d3e4f7": {"is_uaa": True, "is_unicast": True},
   ...     "a0b1c2d3e4f8": {"is_uaa": True, "is_unicast": True},
   ...     "a0b1c2d3e4f9": {"is_uaa": True, "is_unicast": True},
   ...     "a0b1c2d3e4fa": {"is_uaa": True, "is_unicast": True},
   ...     "a0b1c2d3e4fb": {"is_uaa": True, "is_unicast": True},
   ...     "a0b1c2d3e4fc": {"is_uaa": True, "is_unicast": True},
   ...     "a0b1c2d3e4fd": {"is_uaa": True, "is_unicast": True},
   ...     "a0b1c2d3e4fe": {"is_uaa": True, "is_unicast": True},
   ...     "a0b1c2d3e4ff": {"is_uaa": True, "is_unicast": True}
   ... }

   # Call `json.dumps` on the unserialized addresses.

   >>> serialized = dumps(unserialized, indent=2)
   >>> print(serialized)
   {
     "a0b1c2d3e4f5": {
       "is_uaa": true,
       "is_unicast": true
     },
     "a0b1c2d3e4f6": {
       "is_uaa": true,
       "is_unicast": true
     },
     "a0b1c2d3e4f7": {
       "is_uaa": true,
       "is_unicast": true
     },
     "a0b1c2d3e4f8": {
       "is_uaa": true,
       "is_unicast": true
     },
     "a0b1c2d3e4f9": {
       "is_uaa": true,
       "is_unicast": true
     },
     "a0b1c2d3e4fa": {
       "is_uaa": true,
       "is_unicast": true
     },
     "a0b1c2d3e4fb": {
       "is_uaa": true,
       "is_unicast": true
     },
     "a0b1c2d3e4fc": {
       "is_uaa": true,
       "is_unicast": true
     },
     "a0b1c2d3e4fd": {
       "is_uaa": true,
       "is_unicast": true
     },
     "a0b1c2d3e4fe": {
       "is_uaa": true,
       "is_unicast": true
     },
     "a0b1c2d3e4ff": {
       "is_uaa": true,
       "is_unicast": true
     }
   }


Testing macaddress
==================

To conduct testing, run the following commands from your shell.

.. code-block:: console

   [user@host macaddress]$ flake8 --count --ignore E125 macaddress
   [user@host macaddress]$ pytest --cov --cov-report=term-missing


Other languages
===============

The macaddress library is also available in the following languages:

* `JavaScript <https://github.com/critical-path/macaddress-js>`__
* `Ruby <https://github.com/critical-path/macaddress-rb>`__
* `Rust <https://github.com/critical-path/macaddress-rs>`__
