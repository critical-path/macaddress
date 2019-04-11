INVALID_OCTET = [
    "f",             # Too few digits
    "fff",           # Too many digits
    "g"              # Invalid digit
]

OCTET = [
    ("A0", "a0", "10100000", "00000101", "0"),
    ("a0", "a0", "10100000", "00000101", "0"),
    ("B1", "b1", "10110001", "10001101", "1"),
    ("b1", "b1", "10110001", "10001101", "1"),
    ("C2", "c2", "11000010", "01000011", "0"),
    ("c2", "c2", "11000010", "01000011", "0"),
    ("D3", "d3", "11010011", "11001011", "1"),
    ("d3", "d3", "11010011", "11001011", "1"),
    ("E4", "e4", "11100100", "00100111", "0"),
    ("e4", "e4", "11100100", "00100111", "0"),
    ("F5", "f5", "11110101", "10101111", "1"),
    ("f5", "f5", "11110101", "10101111", "1")
]

INVALID_IDENTIFIER = [
    "0a",                 # Too few digits
    "0a1b2c3d4e5f6",      # Too many digits
    "0a1b2c3d4e5g",       # Invalid digit
    "-0a-1b-2c-3d-4e-5f", # Leading hyphen
    "0a-1b-2c-3d-4e-5f-", # Trailing hyphen
    "0a-1b-2c-3d-4e5f",   # Missing hyphen
    ":0a:1b:2c:3d:4e:5f", # Leading colon
    "0a:1b:2c:3d:4e:5f:", # Trailing colon
    "0a:1b:2c:3d:4e5f",   # Missing colon
    ".0a1b.2c3d.4e5f",    # Leading dot
    "0a1b.2c3d.4e5f.",    # Trailing dot
    "0a1b.2c3d4e5f"       # Missing dot
]

EUI = [
    (
        "a0b1c2d3e4f5", # Plain notation (lowercase) 
        "a0b1c2d3e4f5", 
        "101000001011000111000010110100111110010011110101",
        "000001011000110101000011110010110010011110101111",
        ("a0b1c2", "d3e4f5"),
        ("a0b1c2d3e", "4f5"),
        "a0b1c2d3e4f5",
        "a0-b1-c2-d3-e4-f5",
        "a0:b1:c2:d3:e4:f5",
        "a0b1.c2d3.e4f5"
    ),
    (
        "A0B1C2D3E4F5", # Plain notation (uppercase)
        "a0b1c2d3e4f5", 
        "101000001011000111000010110100111110010011110101",
        "000001011000110101000011110010110010011110101111",
        ("a0b1c2", "d3e4f5"),
        ("a0b1c2d3e", "4f5"),
        "a0b1c2d3e4f5",
        "a0-b1-c2-d3-e4-f5",
        "a0:b1:c2:d3:e4:f5",
        "a0b1.c2d3.e4f5"
    ),
    (
        "a0-b1-c2-d3-e4-f5", # Hyphen notation (lowercase)
        "a0b1c2d3e4f5", 
        "101000001011000111000010110100111110010011110101",
        "000001011000110101000011110010110010011110101111",
        ("a0b1c2", "d3e4f5"),
        ("a0b1c2d3e", "4f5"),
        "a0b1c2d3e4f5",
        "a0-b1-c2-d3-e4-f5",
        "a0:b1:c2:d3:e4:f5",
        "a0b1.c2d3.e4f5"
    ),
    (
        "A0-B1-C2-D3-E4-F5", # Hyphen notation (uppercase)
        "a0b1c2d3e4f5", 
        "101000001011000111000010110100111110010011110101",
        "000001011000110101000011110010110010011110101111",
        ("a0b1c2", "d3e4f5"),
        ("a0b1c2d3e", "4f5"),
        "a0b1c2d3e4f5",
        "a0-b1-c2-d3-e4-f5",
        "a0:b1:c2:d3:e4:f5",
        "a0b1.c2d3.e4f5"
    ),
    (
        "a0:b1:c2:d3:e4:f5", # Colon notation (lowercase)
        "a0b1c2d3e4f5", 
        "101000001011000111000010110100111110010011110101",
        "000001011000110101000011110010110010011110101111",
        ("a0b1c2", "d3e4f5"),
        ("a0b1c2d3e", "4f5"),
        "a0b1c2d3e4f5",
        "a0-b1-c2-d3-e4-f5",
        "a0:b1:c2:d3:e4:f5",
        "a0b1.c2d3.e4f5"
    ),
    (
        "A0:B1:C2:D3:E4:F5", # Colon notation (uppercase)
        "a0b1c2d3e4f5", 
        "101000001011000111000010110100111110010011110101",
        "000001011000110101000011110010110010011110101111",
        ("a0b1c2", "d3e4f5"),
        ("a0b1c2d3e", "4f5"),
        "a0b1c2d3e4f5",
        "a0-b1-c2-d3-e4-f5",
        "a0:b1:c2:d3:e4:f5",
        "a0b1.c2d3.e4f5"
    ),
    (
        "a0b1.c2d3.e4f5", # Dot notation (lowercase)
        "a0b1c2d3e4f5", 
        "101000001011000111000010110100111110010011110101",
        "000001011000110101000011110010110010011110101111",
        ("a0b1c2", "d3e4f5"),
        ("a0b1c2d3e", "4f5"),
        "a0b1c2d3e4f5",
        "a0-b1-c2-d3-e4-f5",
        "a0:b1:c2:d3:e4:f5",
        "a0b1.c2d3.e4f5"
    ),
    (
        "A0B1.C2D3.E4F5", # Dot notation (uppercase)
        "a0b1c2d3e4f5", 
        "101000001011000111000010110100111110010011110101",
        "000001011000110101000011110010110010011110101111",
        ("a0b1c2", "d3e4f5"),
        ("a0b1c2d3e", "4f5"),
        "a0b1c2d3e4f5",
        "a0-b1-c2-d3-e4-f5",
        "a0:b1:c2:d3:e4:f5",
        "a0b1.c2d3.e4f5"
    )
]

ELI = [
    (
        "0a1b2c3d4e5f", # Plain notation (lowercase) 
        "0a1b2c3d4e5f", 
        "000010100001101100101100001111010100111001011111",
        "010100001101100000110100101111000111001011111010",
        ("0a1b2c", "3d4e5f"),
        ("0a1b2c3d4", "e5f"),
        "0a1b2c3d4e5f",
        "0a-1b-2c-3d-4e-5f",
        "0a:1b:2c:3d:4e:5f",
        "0a1b.2c3d.4e5f"
    ),
    (
        "0A1B2C3D4E5F", # Plain notation (uppercase)
        "0a1b2c3d4e5f", 
        "000010100001101100101100001111010100111001011111",
        "010100001101100000110100101111000111001011111010",
        ("0a1b2c", "3d4e5f"),
        ("0a1b2c3d4", "e5f"),
        "0a1b2c3d4e5f",
        "0a-1b-2c-3d-4e-5f",
        "0a:1b:2c:3d:4e:5f",
        "0a1b.2c3d.4e5f"
    ),
    (
        "0a-1b-2c-3d-4e-5f", # Hyphen notation (lowercase)
        "0a1b2c3d4e5f", 
        "000010100001101100101100001111010100111001011111",
        "010100001101100000110100101111000111001011111010",
        ("0a1b2c", "3d4e5f"),
        ("0a1b2c3d4", "e5f"),
        "0a1b2c3d4e5f",
        "0a-1b-2c-3d-4e-5f",
        "0a:1b:2c:3d:4e:5f",
        "0a1b.2c3d.4e5f"
    ),
    (
        "0A-1B-2C-3D-4E-5F", # Hyphen notation (uppercase)
        "0a1b2c3d4e5f", 
        "000010100001101100101100001111010100111001011111",
        "010100001101100000110100101111000111001011111010",
        ("0a1b2c", "3d4e5f"),
        ("0a1b2c3d4", "e5f"),
        "0a1b2c3d4e5f",
        "0a-1b-2c-3d-4e-5f",
        "0a:1b:2c:3d:4e:5f",
        "0a1b.2c3d.4e5f"
    ),
    (
        "0a:1b:2c:3d:4e:5f", # Colon notation (lowercase)
        "0a1b2c3d4e5f", 
        "000010100001101100101100001111010100111001011111",
        "010100001101100000110100101111000111001011111010",
        ("0a1b2c", "3d4e5f"),
        ("0a1b2c3d4", "e5f"),
        "0a1b2c3d4e5f",
        "0a-1b-2c-3d-4e-5f",
        "0a:1b:2c:3d:4e:5f",
        "0a1b.2c3d.4e5f"
    ),
    (
        "0A:1B:2C:3D:4E:5F", # Colon notation (uppercase)
        "0a1b2c3d4e5f", 
        "000010100001101100101100001111010100111001011111",
        "010100001101100000110100101111000111001011111010",
        ("0a1b2c", "3d4e5f"),
        ("0a1b2c3d4", "e5f"),
        "0a1b2c3d4e5f",
        "0a-1b-2c-3d-4e-5f",
        "0a:1b:2c:3d:4e:5f",
        "0a1b.2c3d.4e5f"
    ),
    (
        "0a1b.2c3d.4e5f", # Dot notation (lowercase) 
        "0a1b2c3d4e5f", 
        "000010100001101100101100001111010100111001011111",
        "010100001101100000110100101111000111001011111010",
        ("0a1b2c", "3d4e5f"),
        ("0a1b2c3d4", "e5f"),
        "0a1b2c3d4e5f",
        "0a-1b-2c-3d-4e-5f",
        "0a:1b:2c:3d:4e:5f",
        "0a1b.2c3d.4e5f"
    ),
    (
        "0A1B.2C3D.4E5F", # Dot notation (uppercase) 
        "0a1b2c3d4e5f", 
        "000010100001101100101100001111010100111001011111",
        "010100001101100000110100101111000111001011111010",
        ("0a1b2c", "3d4e5f"),
        ("0a1b2c3d4", "e5f"),
        "0a1b2c3d4e5f",
        "0a-1b-2c-3d-4e-5f",
        "0a:1b:2c:3d:4e:5f",
        "0a1b.2c3d.4e5f"
    )
]

NULL_EUI = [
    (
        "ffffffffffff", # Plain notation (lowercase)
        "ffffffffffff",
        "111111111111111111111111111111111111111111111111",
        "111111111111111111111111111111111111111111111111",
        ("ffffff", "ffffff"),
        ("fffffffff", "fff"),
        "ffffffffffff",
        "ff-ff-ff-ff-ff-ff",
        "ff:ff:ff:ff:ff:ff",
        "ffff.ffff.ffff"
    ),
    (
        "FFFFFFFFFFFF", # Plain notation (uppercase)
        "ffffffffffff",
        "111111111111111111111111111111111111111111111111",
        "111111111111111111111111111111111111111111111111",
        ("ffffff", "ffffff"),
        ("fffffffff", "fff"),
        "ffffffffffff",
        "ff-ff-ff-ff-ff-ff",
        "ff:ff:ff:ff:ff:ff",
        "ffff.ffff.ffff"
    ),
    (
        "ff-ff-ff-ff-ff-ff", # Hyphen notation (lowercase)
        "ffffffffffff",
        "111111111111111111111111111111111111111111111111",
        "111111111111111111111111111111111111111111111111",
        ("ffffff", "ffffff"),
        ("fffffffff", "fff"),
        "ffffffffffff",
        "ff-ff-ff-ff-ff-ff",
        "ff:ff:ff:ff:ff:ff",
        "ffff.ffff.ffff"
    ),
    (
        "FF-FF-FF-FF-FF-FF", # Hyphen notation (uppercase)
        "ffffffffffff",
        "111111111111111111111111111111111111111111111111",
        "111111111111111111111111111111111111111111111111",
        ("ffffff", "ffffff"),
        ("fffffffff", "fff"),
        "ffffffffffff",
        "ff-ff-ff-ff-ff-ff",
        "ff:ff:ff:ff:ff:ff",
        "ffff.ffff.ffff"
    ),
    (
        "ff:ff:ff:ff:ff:ff", # Colon notation (lowercase)
        "ffffffffffff",
        "111111111111111111111111111111111111111111111111",
        "111111111111111111111111111111111111111111111111",
        ("ffffff", "ffffff"),
        ("fffffffff", "fff"),
        "ffffffffffff",
        "ff-ff-ff-ff-ff-ff",
        "ff:ff:ff:ff:ff:ff",
        "ffff.ffff.ffff"
    ),
    (
        "FF:FF:FF:FF:FF:FF", # Colon notation (uppercase)
        "ffffffffffff",
        "111111111111111111111111111111111111111111111111",
        "111111111111111111111111111111111111111111111111",
        ("ffffff", "ffffff"),
        ("fffffffff", "fff"),
        "ffffffffffff",
        "ff-ff-ff-ff-ff-ff",
        "ff:ff:ff:ff:ff:ff",
        "ffff.ffff.ffff"
    ),
    (
        "ffff.ffff.ffff", # Dot notation (lowercase)
        "ffffffffffff",
        "111111111111111111111111111111111111111111111111",
        "111111111111111111111111111111111111111111111111",
        ("ffffff", "ffffff"),
        ("fffffffff", "fff"),
        "ffffffffffff",
        "ff-ff-ff-ff-ff-ff",
        "ff:ff:ff:ff:ff:ff",
        "ffff.ffff.ffff"
    ),
    (
        "FFFF.FFFF.FFFF", # Dot notation (uppercase)
        "ffffffffffff",
        "111111111111111111111111111111111111111111111111",
        "111111111111111111111111111111111111111111111111",
        ("ffffff", "ffffff"),
        ("fffffffff", "fff"),
        "ffffffffffff",
        "ff-ff-ff-ff-ff-ff",
        "ff:ff:ff:ff:ff:ff",
        "ffff.ffff.ffff"
    )
]

INVALID_ADDRESS = INVALID_IDENTIFIER

BROADCAST = "ffffffffffff"

MULTICAST = "0180c2000000"  # Link-Layer Discovery Protocol

UAA_UNICAST = "a0b1c2d3e4f5"

LAA_UNICAST = "aab1c2d3e4f5"
