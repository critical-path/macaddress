"""
This module includes Octet and OctetError.
"""

from functools import reduce

import re


DIGITS = re.compile("^[0-9A-Fa-f]{2}$")


class OctetError(Exception):
    """
    Octet raises OctetError if instantiated with an invalid argument.

    Parameters
    ----------
    message : str
        A human-readable error message.
    """

    pass


class Octet(object):
    """
    Octet makes it easy to convert two hexadecimal digits to eight
    binary or reverse-binary digits.

    This is useful when working with the IEEE's extended unique
    identifiers and extended local identifiers.

    Attributes
    ----------
    original : str
        The hexadecimal digits passed in by the user.

    normalized : str
        The hexadecimal digits after replacing all uppercase
        letters with lowercase letters.

        For example, if the user passes in `A0`, then Octet
        will return `a0`.

    is_valid : bool
        Whether the user passed in valid hexadecimal digits.

    binary : str
        The binary equivalent of the hexadecimal digits passed
        in by the user.  *The most-significant digit appears first.*

        For example, if the user passes in `A0`, then Octet
        will return `10100000`.

    reverse_binary : str
        The reverse-binary equivalent of the hexadecimal digits
        passed in by the user.  *The least-significant digit
        appears first.*

        For example, if the user passes in `A0`, then Octet
        will return `00000101`.

    Parameters
    ----------
    digits : str
        Two hexadecimal digits (0-9, A-F, or a-f).

    Raises
    ------
    OctetError
    """

    def __init__(self, digits):
        self.original = digits

        if not self.is_valid:
            raise OctetError("Pass in two hexadecimal digits.")

    def __repr__(self):
        return "Octet('{}')".format(self.original)

    def __str__(self):
        return self.normalized

    @property
    def is_valid(self):
        # Evaluate the hexadecimal digits.

        if DIGITS.match(self.original):
            return True
        else:
            return False

    @property
    def normalized(self):
        return self.original.lower()

    @property
    def binary(self):
        # Convert from hexadecimal digits to decimal digits and
        # then from decimal digits to binary digits.  Pad with
        # zeroes as necessary.

        decimal = int(self.normalized, base=16)
        return format(decimal, "b").zfill(8)

    @property
    def reverse_binary(self):
        # Concatenate the binary digits in reverse order.

        return reduce(lambda x, y: x + y, reversed(self.binary))

    def bit(self, index):
        """
        Returns a binary bit.

        Parameters
        ----------
        index : int
            The index of the binary bit to return.
        """

        try:
            return self.binary[index]
        except IndexError:
            pass
