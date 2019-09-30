"""
This module includes ExtendedIdentifier48 and IdentifierError.
"""

from functools import reduce

import re

from macaddress.octet import Octet


PLAIN = re.compile("^[0-9A-Fa-f]{12}$")
HYPHEN = re.compile("^([0-9A-Fa-f]{2}[-]{1}){5}[0-9A-Fa-f]{2}$")
COLON = re.compile("^([0-9A-Fa-f]{2}[:]{1}){5}[0-9A-Fa-f]{2}$")
DOT = re.compile("^([0-9A-Fa-f]{4}[.]{1}){2}[0-9A-Fa-f]{4}$")
NOT_DIGITS = re.compile("[^0-9A-Fa-f]")
TWO_DIGITS = re.compile("[0-9a-f]{2}")
FOUR_DIGITS = re.compile("[0-9a-f]{4}")


class IdentifierError(Exception):
    """
    ExtendedIdentifier48 raises IdentifierError if instantiated
    with an invalid argument.

    Arguments
    ---------
    message : str
        A human-readable error message.
    """

    pass


class ExtendedIdentifier48(object):
    """
    ExtendedIdentifier48 makes it easy to work with the IEEE's 48-bit
    extended unique identifiers (EUI) and extended local identifiers (ELI).

    The first 24 or 36 bits of an EUI is called an organizationally-
    unique identifier (OUI), while the first 24 or 36 bits of an ELI is
    called a company ID (CID).

    Visit the IEEE's website for more information on EUIs and ELIs.

    Helpful link:
    https://standards.ieee.org/products-services/regauth/tut/index.html

    Attributes
    ----------
    original : str
        The hexadecimal identifier passed in by the user.

    normalized : str
        The hexadecimal identifier after replacing all uppercase
        letters with lowercase letters and removing all hypens,
        colons, and dots.

        For example, if the user passes in `A0-B1-C2-D3-E4-F5`,
        then ExtendedIdentifier48 will return `a0b1c2d3e4f5`.

    is_valid : bool
        Whether the user passed in a valid hexadecimal identifier.

    octets : list
        Each of the hexadecimal identifier's six octets.

    first_octet : Octet
        The hexadecimal identifier's first octet.

    type : str
        The hexadecimal identifier's type, where type is unique,
        local, or unknown.

        The two least-significant bits in the first octet of
        an extended identifier determine whether it is an EUI.

        00 = unique.

        The four least-signficant bits in the first octet of
        an extended identifier determine whether it is an ELI.

        1010 = local.

    has_oui : bool
        Whether the hexadecimal identifier has an OUI.

        If the identifier is an EUI, then it has an OUI.

    has_cid : bool
        Whether the hexadecimal identifier has a CID.

        If the identifier is an ELI, then it has a CID.

    binary : str
        The binary equivalent of the hexadecimal identifier passed
        in by the user.  *The most-significant digit of each
        octet appears first.*

        For example, if the user passes in `A0-B1-C2-D3-E4-F5`,
        then ExtendedIdentifier48 will return
        `101000001011000111000010110100111110010011110101`.

    reverse_binary : str
        The reverse-binary equivalent of the hexadecimal identifier
        passed in by the user.  *The least-significant digit of
        each octet appears first.*

        For example, if the user passes in `A0-B1-C2-D3-E4-F5`,
        then ExtendedIdentifier48 will return
        `000001011000110101000011110010110010011110101111`.

    Parameters
    ----------
    identifier : str
        Twelve hexadecimal digits (0-9, A-F, or a-f).

    Raises
    ------
    IdentifierError
    """

    def __init__(self, identifier):
        self.original = identifier

        if not self.is_valid:
            raise IdentifierError("Pass in 12 hexadecimal digits.")

    def __repr__(self):
        return "ExtendedIdentifier48('{}')".format(self.original)

    def __str__(self):
        return self.normalized

    @property
    def is_valid(self):
        # Evaluate the hexadecimal identifier.
        # It must contain 12 hexadecimal digits, and it may
        # be in plain, hyphen, colon, or dot notation.

        if PLAIN.match(self.original):
            return True
        elif HYPHEN.match(self.original):
            return True
        elif COLON.match(self.original):
            return True
        elif DOT.match(self.original):
            return True
        else:
            return False

    @property
    def normalized(self):
        return NOT_DIGITS.sub("", self.original.lower())

    @property
    def octets(self):
        # Create one instance of Octet for each of the
        # hexadecimal identifier's six octets.

        matches = TWO_DIGITS.findall(self.normalized)
        return [Octet(match) for match in matches]

    @property
    def first_octet(self):
        return self.octets[0]

    @property
    def type(self):
        # The two least-significant bits in the first octet of
        # an extended identifier determine whether it is an EUI.

        # The four least-signficant bits in the first octet of
        # an extended identifier determine whether it is an ELI.

        if self.first_octet.binary[6:8] == "00":
            return "unique"
        elif self.first_octet.binary[4:8] == "1010":
            return "local"
        else:
            return "unknown"

    @property
    def has_oui(self):
        # If the hexadecimal identifier is an EUI, then it has an OUI.

        return self.type == "unique"

    @property
    def has_cid(self):
        # If the hexadecimal identifier is an ELI, then it has a CID.

        return self.type == "local"

    @property
    def binary(self):
        binaries = map(lambda x: x.binary, self.octets)
        return reduce(lambda x, y: x + y, binaries)

    @property
    def reverse_binary(self):
        reverse_binaries = map(lambda x: x.reverse_binary, self.octets)
        return reduce(lambda x, y: x + y, reverse_binaries)

    def to_fragments(self, bits=24):
        """
        Returns the hexadecimal identifier's two "fragments."

        For an EUI, this means the 24- or 36-bit OUI as the first
        fragment and the remaining device- or object-specific bits
        as the second fragment.

        For an ELI, this means the 24- or 36-bit CID as the first
        fragment and the remaining device- or object-specific bits
        as the second fragment.

        For example, if the user passes in `A0-B1-C2-D3-E4-F5` and
        calls this method with either `bits=24` or no keyword argument,
        then ExtendedIdentifier48 will return `(a0b1c2, d3e4f5)`.

        If the user passes in `A0-B1-C2-D3-E4-F5` and calls this method
        with `bits=36`, then ExtendedIdentifier48 will return
        `(a0b1c2d3e, 4f5)`.

        Parameters
        ----------
        bits : int
            The number of bits for the OUI or CID.

            The default value is 24.
        """

        digits = int(bits / 4)
        return (self.normalized[:digits], self.normalized[digits:])

    def to_plain_notation(self):
        """
        Returns the hexadecimal identifier in plain notation
        (for example, `a0b1c2d3e4f5`).
        """

        return self.normalized

    def to_hyphen_notation(self):
        """
        Returns the hexadecimal identifier in hyphen notation
        (for example, `a0-b1-c2-d3-e4-f5`).
        """

        matches = TWO_DIGITS.findall(self.normalized)
        return "-".join(matches)

    def to_colon_notation(self):
        """
        Returns the hexadecimal identifier in colon notation
        (for example, `a0:b1:c2:d3:e4:f5`).
        """

        matches = TWO_DIGITS.findall(self.normalized)
        return ":".join(matches)

    def to_dot_notation(self):
        """
        Returns the hexadecimal identifier in dot notation
        (for example, `a0b1.c2d3.e4f5`).
        """

        matches = FOUR_DIGITS.findall(self.normalized)
        return ".".join(matches)
