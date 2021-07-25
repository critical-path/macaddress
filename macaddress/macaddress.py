"""
This module includes MediaAccessControlAddress and AddressError.
"""


from .ei48 import (
    ExtendedIdentifier48,
    IdentifierError
)


class AddressError(Exception):
    """
    MediaAccessControlAddress raises AddressError if instantiated
    with an invalid argument.

    Arguments
    ---------
    message : str
        A human-readable error message.
    """

    pass


class MediaAccessControlAddress(ExtendedIdentifier48):
    """
    MediaAccessControlAddress makes it easy to work with media access
    control (MAC) addresses.

    Attributes
    ----------
    is_broadcast : bool
        Whether the MAC address is a broadcast address.

        "ffffffffffff" = broadcast.

    is_multicast : bool
        Whether the MAC address is a multicast address
        (layer-two multicast, not layer-three multicast).

        The least-significant bit in the first octet of a MAC address
        determines whether it is a multicast or a unicast.

        1 = multicast.

    is_unicast : bool
        Whether the MAC address is a unicast address.

        The least-significant bit in the first octet of a MAC address
        determines whether it is a multicast or a unicast.

        0 = unicast.

    is_uaa : bool
        Whether the MAC address is a universally-administered
        address (UAA).

        The second-least-significant bit in the first octet of a MAC
        address determines whether it is a UAA or an LAA.

        0 = UAA.

    is_laa : bool
        Whether the MAC address is a locally-administered
        address (LAA).

        The second-least-significant bit in the first octet of a MAC
        address determines whether it is a UAA or an LAA.

        1 = LAA.
    """

    def __init__(self, address):
        try:
            super().__init__(address)
        except IdentifierError:
            raise AddressError("Pass in 12 hexadecimal digits.")

    def __repr__(self):
        return "MediaAccessControlAddress('{}')".format(self.original)

    def __str__(self):
        return self.normalized

    @property
    def is_broadcast(self):
        return self.normalized == "ffffffffffff"

    @property
    def is_multicast(self):
        # The least-significant bit in the first octet of a MAC address
        # determines whether it is a multicast or a unicast.

        return self.first_octet.binary[7] == "1"

    @property
    def is_unicast(self):
        return not self.is_multicast

    @property
    def is_uaa(self):
        # The second-least-significant bit in the first octet of a MAC
        # address determines whether it is a UAA or an LAA.

        return self.is_unicast and self.first_octet.binary[6] == "0"

    @property
    def is_laa(self):
        # The second-least-significant bit in the first octet of a MAC
        # address determines whether it is a UAA or an LAA.

        return self.is_unicast and self.first_octet.binary[6] == "1"
