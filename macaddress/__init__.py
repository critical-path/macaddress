"""
The macaddress library makes it easy to work with media access control
(MAC) addresses.
"""


__author__ = "critical-path"

__version__ = "0.7.0"

__all__ = [
    "ExtendedIdentifier48",
    "MediaAccessControlAddress",
    "Octet",
    "IdentifierError",
    "AddressError",
    "OctetError"
]


from macaddress.ei48 import (
    ExtendedIdentifier48,
    IdentifierError
)

from macaddress.macaddress import (
    MediaAccessControlAddress,
    AddressError
)

from macaddress.octet import (
    Octet,
    OctetError
)
