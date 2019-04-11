[![Build Status](https://travis-ci.com/critical-path/macaddress.svg?branch=master)](https://travis-ci.com/critical-path/macaddress) [![Coverage Status](https://coveralls.io/repos/github/critical-path/macaddress/badge.svg)](https://coveralls.io/github/critical-path/macaddress)

## macaddress v0.1.0

The macaddress library makes it easy to work with media access control (MAC) addresses.


## Dependencies

macaddress requires Python 3.x and the pip package.  It also requires the following packages for testing.

__Testing__:
- coveralls
- flake8
- pytest
- pytest-cov


## Installing macaddress with test cases and testing dependencies

1. Clone or download this repository.

2. Using `sudo`, run `pip` with the `install` command and the `--editable` option.

```
sudo pip install --editable .[test]
```


## Installing macaddress without test cases or testing dependencies

1. Clone or download this repository.

2. Using `sudo`, run `pip` with the `install` command.

```
sudo pip install .
```


## Using macaddress

Import `MediaAccessControlAddress`.

```python
>>> from macaddress import MediaAccessControlAddress
```

Instantiate `MediaAccessControlAddress` with a MAC address in plain, hyphen, colon, or dot notation.

```python
>>> mac = MediaAccessControlAddress("a0b1c2d3e4f5")
```

```python
>>> mac = MediaAccessControlAddress("a0-b1-c2-d3-e4-f5")
```

```python
>>> mac = MediaAccessControlAddress("a0:b1:c2:d3:e4:f5")
```

```python
>>> mac = MediaAccessControlAddress("a0b1.c2d3.e4f5")
```

To determine whether the MAC address is a broadcast, multicast (layer-two), or unicast, access its `is_broadcast`, `is_multicast`, and `is_unicast` properties.

```python
>>> print(mac.is_broadcast)
False
```

```python
>>> print(mac.is_multicast)
False
```

```python
>>> print(mac.is_unicast)
True
```

To determine whether the MAC address is a universally-administered address (UAA) or a locally-administered address (LAA), access its `is_uaa` and `is_laa` properties.

```python
>>> print(mac.is_uaa)
True
```

```python
>>> print(mac.is_laa)
False
```

To work with the MAC address's octets, access its `octets` property.  It contains one `Octet` object for each of the address's six octets.

```python
>>> print(mac.octets)
[Octet('a0'), Octet('b1'), Octet('c2'), Octet('d3'), Octet('e4'), Octet('f5')]
```

To determine whether the MAC address is an extended unique identifier (EUI), an extended local identifier (ELI), or unknown, access its `type` property.

```python
>>> print(mac.type)
unique
```

To determine whether the MAC address has an organizationally-unique identifier (OUI) or a company ID, access its `has_oui` and `has_cid` properties.

```python
>>> print(mac.has_oui)
True
```

```python
>>> print(mac.has_cid)
False
```

To view the binary equivalent of the MAC address, access its `binary` and `reverse_binary` properties. With `binary`, the most-significant digit of each octet appears first.  With `reverse_binary`, the least-significant digit of each octet appears first.

```python
>>> print(mac.binary)
101000001011000111000010110100111110010011110101
```

```python
>>> print(mac.reverse_binary)
000001011000110101000011110010110010011110101111
```

To return the MAC address's two "fragments," call the `to_fragments` method.  For an EUI, this means the 24- or 36-bit OUI as the first fragment and the remaining device- or object-specific bits as the second fragment.  For an ELI, this means the 24- or 36-bit CID as the first fragment and the remaining device- or object-specific bits as the second fragment.

```python
>>> fragments_without_keyword_argument = mac.to_fragments()
>>> print(fragments_without_keyword_argument)
('a0b1c2', 'd3e4f5')
```

```python
>>> fragments_with_24_bits = mac.to_fragments(bits=24)
>>> print(fragments_with_24_bits)
('a0b1c2', 'd3e4f5')
```

```python
>>> fragments_with_36_bits = mac.to_fragments(bits=36)
>>> print(fragments_with_36_bits)
('a0b1c2d3e', '4f5')
```

To return the MAC address in different notations, call the `to_plain_notation`, `to_hyphen_notation`, `to_colon_notation`, and `to_dot_notation` methods.

```python
>>> plain = mac.to_plain_notation()
>>> print(plain)
a0b1c2d3e4f5
```

```python
>>> hyphen = mac.to_hyphen_notation()
>>> print(hyphen)
a0-b1-c2-d3-e4-f5
```

```python
>>> colon = mac.to_colon_notation()
>>> print(colon)
a0:b1:c2:d3:e4:f5
```

```python
>>> dot = mac.to_dot_notation()
>>> print(dot)
a0b1.c2d3.e4f5
```


## Testing macaddress after installation

1. Run `flake8` with the `--count` and `--ignore` options.

```
flake8 --count --ignore E125 macaddress
```

2. Run `pytest` with the `--cov`, and `--cov-report` options.

```
pytest --cov --cov-report=term-missing
```


## A note on OUIs, CIDs, UAAs, and LAAs

It appears that all OUIs are UAAs, all UAAs are OUIs, all CIDs are LAAs, but not all LAAs are CIDs.
