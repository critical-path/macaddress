"""
The macaddress library makes it easy to work with media access control
(MAC) addresses.
"""


__author__ = "critical-path"

__version__ = "0.10.1"

__all__ = [
    "ExtendedIdentifier48",
    "MediaAccessControlAddress",
    "Octet",
    "IdentifierError",
    "AddressError",
    "OctetError"
]


from .ei48 import (
    ExtendedIdentifier48,
    IdentifierError
)

from .macaddress import (
    MediaAccessControlAddress,
    AddressError
)

from .octet import (
    Octet,
    OctetError
)
