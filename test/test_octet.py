from pytest import (
    mark,
    raises
)

from macaddress.octet import (
    Octet,
    OctetError
)

from constants import (
    INVALID_OCTET,
    OCTET
)


@mark.parametrize("digits", INVALID_OCTET)
def test_octet_error(digits):
    with raises(OctetError) as exception:
        octet = Octet(digits)

    assert "Pass in two hexadecimal digits." == str(exception.value)


@mark.parametrize(
    ("original", "normalized","binary", "reverse_binary"), 
    OCTET
)
def test_octet(original, normalized, binary, reverse_binary, capsys):
    # Instantiate Octet

    octet = Octet(original)

    # Test properties

    assert octet.original == original
    assert octet.normalized == normalized
    assert octet.is_valid == True
    assert octet.binary == binary
    assert octet.reverse_binary == reverse_binary

    # Test __repr__

    assert repr(octet) == "Octet('{}')".format(original)

    # Test __str__

    print(octet)
    stdout, stderr = capsys.readouterr()
    assert stdout == normalized + "\n"
