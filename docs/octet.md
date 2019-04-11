## Introduction

`ExtendedIdentifier48` relies upon `Octet` to convert hexadecimal digits to their binary and reverse-binary equivalents.  This file describes how to use `Octet` on its own.

## Using Octet

Import `Octet`.

```python
>>> from macaddress import Octet
```

Instantiate `Octet`, passing in two hexadecimal digits.  `Octet` accepts both uppercase letters and lowercase letters.

```python
>>> digits = "a0"
>>> octet = Octet(digits)
```

To view the binary equivalent of the hexadecimal digits, access the octet's `binary` and `reverse_binary` properties.  With `binary`, the most-significant digit appears first.  With `reverse_binary`, the least-significant digit appears first.

```python
>>> print(octet.binary)
10100000
```

```python
>>> print(octet.reverse_binary)
00000101
```

To return a particular binary bit, call the `bit` method with an index number.  For example, to return the least-significant digit, pass in `-1`.

```python
>>> least_significant_digit = octet.bit(-1)
>>> print(least_significant_digit)
0
```
