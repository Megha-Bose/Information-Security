## Pseudo-random Generator
A provably-secure pseudo-random generator which outputs a pseudo-random bit-string value of length l(k) when the in-class function generate() is invoked.

## Pseudo-random Function
A provably-secure pseudo-random function that outputs a pseudo-random integer value when the in-class function evaluate() is invoked.

## Encryption Scheme against Eavesdropping Adversary
A secure encryption-decryption scheme for an eavesdropping attack. The encryption and the decryption functionalities are implemented in two different functions.

## CPA-Secure Encryption Scheme
A CPA-secure encryption-decryption scheme using the previously implemented PRF that outputs the ciphertext when the in-class function enc() is invoked and returns the plaintext when the in-class function dec() is invoked.

## Message Authentication Codes
A variable-length message authentication code scheme that returns the tag when the in-class function mac() is invoked and returns a boolean value (0 if the verification is erroneous, 1 otherwise) when the function vrfy() is invoked.

## CBC-MAC
A variable-length CBC-MAC using the previously implemented PRF.

## CCA-Secure Encryption Scheme
A CCA secure scheme using the CPA and CBC-MAC implementations that returns the cipher-text when then in-class function enc() is invoked and returns the plain-text (or not) when the in-class function dec() is invoked. 

Codes are in respective directories with security proofs for the constructions. IO diretory contains sample I/O for each problem.
