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

   # Import "functools.reduce`, `pprint.pprint`, and 
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
