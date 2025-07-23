# Discrete Mathematics Project- RSA Encryption

### Student Name: Saghar Sharifi
### Student ID: 40322113

## What is RSA Encryption?
RSA is an asymmetric encryption algorithm that uses two keys:
- A public key (n, e) to encrypt data
- A private key (n, d) to decrypt it
It relies on the difficulty of factoring large prime numbers. The algorithm works as follows:
  1. Generate two large primes p and q, compute n = p * q
  2. Calculate Euler's totient ((p - 1) (q - 1))
  3. Choose a public exponent e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
  4. Compute the private exponent d such that e × d ≡ 1 (mod φ(n))
  5. To encrypt a message M:
     C = M^e mod n
     To decrypt:
     M = C^d mod n

## Project Objective
This project demonstrates a working RSA encryption system built entirely in Python. It handles:
- Generating keys (public key and private key)
- Encrypting and decrypting **Unicode** (English, Persian, emojis, symbols, ...)
- Basic **manual block processing** for long messages
- Tests to verify correct decryption on different inputs

    The goal was to build something simple, understandable, and still flexible enough to go beyond basic ASCII -something usable with real-world text.

## Technical details
- Keys use 256-bit primes (quick yet safe for academic demo)
- Public exponent e = 65537 (commonly used)
- Uses int.from_bytes() and .to_bytes() to fully support UTF-8 encoding
- Encrypts the message as an integer and converts back to text upon decryption
- There is no advanced padding (OAEP) -this is intentional for transparency and clarity

## Disclaimer
This is for educational purposes only. It does not implement secure cryptographic padding, and should not be used to protect real data.

## How to Run
### Run the main script:
```bash python scr/main.py```

## Project Structure
DMath_FinalProject_4032/
│
├── README.md               # Project overview, usage, and documentation
├── src/                    # Source code directory
│   ├── base.py             #RSA Implementation
│   └── main.py             #CLI Interface
├── input-output/           # Sample input/output for encryption/decryption
│   ├── plaintext_samples.txt
│   ├── ciphertext_samples.txt
│   └── decrypted_results.txt
│
└── report.pdf              # Final report explaining the implementation

## Resources

- [RSA (cryptosystem) on Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) – General overview of RSA.
- [How RSA Works – Numberphile video](https://www.youtube.com/watch?v=wXB-V_Keiu8) – Great visual explanation of RSA encryption.
- [RSA Encryption – Khan Academy](https://www.khanacademy.org/computing/computer-science/cryptography/modern-crypt/v/rsa-encryption) – Beginner-friendly RSA tutorial.
- [Handbook of Applied Cryptography – Chapter 8 (PDF)](https://cacr.uwaterloo.ca/hac/about/chap8.pdf) – In-depth explanation of RSA theory and math.
- [Real Python – Introduction to Cryptography](https://realpython.com/python-cryptography/) – Useful if integrating Python crypto libraries.
- [Python pow() function documentation](https://docs.python.org/3/library/functions.html#pow) – Built-in modular exponentiation used in RSA.
- [PyCryptodome Documentation (Advanced)](https://pycryptodome.readthedocs.io/en/latest/) – For implementing cryptographic operations using a library.


