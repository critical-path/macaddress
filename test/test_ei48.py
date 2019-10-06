from pytest import (
    mark,
    raises
)

from macaddress.ei48 import (
    ExtendedIdentifier48,
    IdentifierError
)

from macaddress.octet import Octet

from constants import (
    INVALID_IDENTIFIER,
    EUI,
    ELI,
    NULL_EUI
)


@mark.parametrize("identifier", INVALID_IDENTIFIER)
def test_identifier_error(identifier):
    with raises(IdentifierError) as exception:
        ei48 = ExtendedIdentifier48(identifier)

    assert "Pass in 12 hexadecimal digits." == str(exception.value)


@mark.parametrize(
    (
        "original", 
        "normalized",
        "decimal",
        "binary", 
        "reverse_binary",
        "fragments_with_24_bit_oui",
        "fragments_with_36_bit_oui",
        "plain",
        "hyphen",
        "colon",
        "dot"
    ), 
    EUI
)
def test_eui(
    original, 
    normalized, 
    decimal,
    binary, 
    reverse_binary,
    fragments_with_24_bit_oui,
    fragments_with_36_bit_oui,
    plain,
    hyphen,
    colon,
    dot,
    capsys
):
    # Instantiate ExtendedIdentifier48

    ei48 = ExtendedIdentifier48(original)

    # Test properties

    assert ei48.original == original
    assert ei48.normalized == normalized
    assert ei48.is_valid == True
    assert len(ei48.octets) == 6
    assert isinstance(ei48.first_octet, Octet)
    assert ei48.type == "unique"
    assert ei48.has_oui == True
    assert ei48.has_cid == False
    assert ei48.decimal == decimal
    assert ei48.binary == binary
    assert ei48.reverse_binary == reverse_binary
    assert ei48.to_fragments() == fragments_with_24_bit_oui
    assert ei48.to_fragments(bits=36) == fragments_with_36_bit_oui
    assert ei48.to_plain_notation() == plain
    assert ei48.to_hyphen_notation() == hyphen
    assert ei48.to_colon_notation() == colon
    assert ei48.to_dot_notation() == dot

    # Test __repr__

    assert repr(ei48) == "ExtendedIdentifier48('{}')".format(original)

    # Test __str__

    print(ei48)
    stdout, stderr = capsys.readouterr()
    assert stdout == normalized + "\n"


@mark.parametrize(
    (
        "original", 
        "normalized",
        "decimal",
        "binary", 
        "reverse_binary",
        "fragments_with_24_bit_oui",
        "fragments_with_36_bit_oui",
        "plain",
        "hyphen",
        "colon",
        "dot"
    ), 
    ELI
)
def test_eli(
    original, 
    normalized, 
    decimal,
    binary, 
    reverse_binary,
    fragments_with_24_bit_oui,
    fragments_with_36_bit_oui,
    plain,
    hyphen,
    colon,
    dot,
    capsys
):
    # Instantiate ExtendedIdentifier48

    ei48 = ExtendedIdentifier48(original)

    # Test properties

    assert ei48.original == original
    assert ei48.normalized == normalized
    assert ei48.is_valid == True
    assert len(ei48.octets) == 6
    assert isinstance(ei48.first_octet, Octet)
    assert ei48.type == "local"
    assert ei48.has_oui == False
    assert ei48.has_cid == True
    assert ei48.decimal == decimal
    assert ei48.binary == binary
    assert ei48.reverse_binary == reverse_binary
    assert ei48.to_fragments() == fragments_with_24_bit_oui
    assert ei48.to_fragments(bits=36) == fragments_with_36_bit_oui
    assert ei48.to_plain_notation() == plain
    assert ei48.to_hyphen_notation() == hyphen
    assert ei48.to_colon_notation() == colon
    assert ei48.to_dot_notation() == dot

    # Test __repr__

    assert repr(ei48) == "ExtendedIdentifier48('{}')".format(original)

    # Test __str__

    print(ei48)
    stdout, stderr = capsys.readouterr()
    assert stdout == normalized + "\n"


@mark.parametrize(
    (
        "original", 
        "normalized",
        "decimal",
        "binary", 
        "reverse_binary",
        "fragments_with_24_bit_oui",
        "fragments_with_36_bit_oui",
        "plain",
        "hyphen",
        "colon",
        "dot"
    ), 
    NULL_EUI
)
def test_null_eui(
    original, 
    normalized,
    decimal,
    binary, 
    reverse_binary,
    fragments_with_24_bit_oui,
    fragments_with_36_bit_oui,
    plain,
    hyphen,
    colon,
    dot,
    capsys
):
    # Instantiate ExtendedIdentifier48

    ei48 = ExtendedIdentifier48(original)

    # Test properties

    assert ei48.original == original
    assert ei48.normalized == normalized
    assert ei48.is_valid == True
    assert len(ei48.octets) == 6
    assert isinstance(ei48.first_octet, Octet)
    assert ei48.type == "unknown"
    assert ei48.has_oui == False
    assert ei48.has_cid == False
    assert ei48.decimal == decimal
    assert ei48.binary == binary
    assert ei48.reverse_binary == reverse_binary
    assert ei48.to_fragments() == fragments_with_24_bit_oui
    assert ei48.to_fragments(bits=36) == fragments_with_36_bit_oui
    assert ei48.to_plain_notation() == plain
    assert ei48.to_hyphen_notation() == hyphen
    assert ei48.to_colon_notation() == colon
    assert ei48.to_dot_notation() == dot

    # Test __repr__

    assert repr(ei48) == "ExtendedIdentifier48('{}')".format(original)

    # Test __str__

    print(ei48)
    stdout, stderr = capsys.readouterr()
    assert stdout == normalized + "\n"
