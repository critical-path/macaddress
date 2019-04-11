"""
The macaddress library makes it easy to work with media access control
(MAC) addresses.
"""


__author__ = "critical-path"

__version__ = "0.1.0"

__all__ = [
    "ExtendedIdentifier48",
    "MediaAccessControlAddress",
    "Octet"
]


from macaddress.ei48 import ExtendedIdentifier48

from macaddress.macaddress import MediaAccessControlAddress

from macaddress.octet import Octet
