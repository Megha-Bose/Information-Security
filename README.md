# Information-Security

**Principles of Information Security** course assignments.

## *Assignment 1*

### Pseudo-random Generator
A provably-secure pseudo-random generator which outputs a pseudo-random bit-string value of length l(k) when the in-class function generate() is invoked.

[Code](A1/PRG/PRG.py) | [Proof of Security](A1/PRG/PRG.pdf)

### Pseudo-random Function
A provably-secure pseudo-random function that outputs a pseudo-random integer value when the in-class function evaluate() is invoked.

[Code](A1/PRF/PRF.py) | [Proof of Security](A1/PRF/PRF.pdf)

### Encryption Scheme against Eavesdropping Adversary
A secure encryption-decryption scheme for an eavesdropping attack. The encryption and the decryption functionalities are implemented in two different functions.

[Code](A1/EAV/EAV.py) | [Proof of Security](A1/EAV/EAV.pdf)

### CPA-Secure Encryption Scheme
A CPA-secure encryption-decryption scheme using the previously implemented PRF that outputs the ciphertext when the in-class function enc() is invoked and returns the plaintext when the in-class function dec() is invoked.

[Code](A1/CPA/CPA.py) | [Proof of Security](A1/CPA/CPA.pdf)

### Message Authentication Codes
A variable-length message authentication code scheme that returns the tag when the in-class function mac() is invoked and returns a boolean value (0 if the verification is erroneous, 1 otherwise) when the function vrfy() is invoked.

[Code](A1/MAC/MAC.py) | [Proof of Security](A1/MAC/MAC.pdf)

### CBC-MAC
A variable-length CBC-MAC using the previously implemented PRF.

[Code](A1/CBC-MAC/CBC-MAC.py) | [Proof of Security](A1/CBC-MAC/CBC-MAC.pdf)

### CCA-Secure Encryption Scheme
A CCA secure scheme using the CPA and CBC-MAC implementations that returns the cipher-text when then in-class function enc() is invoked and returns the plain-text (or not) when the in-class function dec() is invoked. 

[Code](A1/CCA/CCA.py) | [Proof of Security](A1/CCA/CCA.pdf)

