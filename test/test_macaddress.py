from pytest import (
    mark,
    raises
)

from macaddress.macaddress import (
    AddressError,
    MediaAccessControlAddress
)

from constants import (
    INVALID_ADDRESS,
    BROADCAST,
    MULTICAST,
    UAA_UNICAST,
    LAA_UNICAST
)


@mark.parametrize("address", INVALID_ADDRESS)
def test_address_error(address):
    with raises(AddressError) as exception:
        mac = MediaAccessControlAddress(address)

    assert "Pass in 12 hexadecimal digits." == str(exception.value)



def test_broadcast(capsys):

    # Instantiate MediaAccessControlAddress

    mac = MediaAccessControlAddress(BROADCAST)

    # Test properties

    assert mac.is_broadcast == True
    assert mac.is_multicast == True
    assert mac.is_unicast == False
    assert mac.is_uaa == False
    assert mac.is_laa == False

    # Test some inherited properties

    assert mac.type == "unknown"
    assert mac.has_oui == False
    assert mac.has_cid == False

    # Test __repr__

    assert repr(mac) == "MediaAccessControlAddress('{}')".format(BROADCAST)

    # Test __str__

    print(mac)
    stdout, stderr = capsys.readouterr()
    assert stdout == BROADCAST.lower() + "\n"


def test_multicast(capsys):

    # Instantiate MediaAccessControlAddress

    mac = MediaAccessControlAddress(MULTICAST)

    # Test properties

    assert mac.is_broadcast == False
    assert mac.is_multicast == True
    assert mac.is_unicast == False
    assert mac.is_uaa == False
    assert mac.is_laa == False

    # Test some inherited properties

    assert mac.type == "unknown"
    assert mac.has_oui == False
    assert mac.has_cid == False

    # Test __repr__

    assert repr(mac) == "MediaAccessControlAddress('{}')".format(MULTICAST)

    # Test __str__

    print(mac)
    stdout, stderr = capsys.readouterr()
    assert stdout == MULTICAST.lower() + "\n"


def test_uaa_unicast(capsys):

    # Instantiate MediaAccessControlAddress

    mac = MediaAccessControlAddress(UAA_UNICAST)

    # Test properties

    assert mac.is_broadcast == False
    assert mac.is_multicast == False
    assert mac.is_unicast == True
    assert mac.is_uaa == True
    assert mac.is_laa == False

    # Test some inherited properties

    assert mac.type == "unique"
    assert mac.has_oui == True
    assert mac.has_cid == False

    # Test __repr__

    assert repr(mac) == "MediaAccessControlAddress('{}')".format(UAA_UNICAST)

    # Test __str__

    print(mac)
    stdout, stderr = capsys.readouterr()
    assert stdout == UAA_UNICAST.lower() + "\n"


def test_laa_unicast(capsys):

    # Instantiate MediaAccessControlAddress

    mac = MediaAccessControlAddress(LAA_UNICAST)

    # Test properties

    assert mac.is_broadcast == False
    assert mac.is_multicast == False
    assert mac.is_unicast == True
    assert mac.is_uaa == False
    assert mac.is_laa == True

    # Test some inherited properties

    assert mac.type == "local"
    assert mac.has_oui == False
    assert mac.has_cid == True

    # Test __repr__

    assert repr(mac) == "MediaAccessControlAddress('{}')".format(LAA_UNICAST)

    # Test __str__

    print(mac)
    stdout, stderr = capsys.readouterr()
    assert stdout == LAA_UNICAST.lower() + "\n"
