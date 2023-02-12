from typing import Optional


class CPA:
    def __init__(self, security_parameter: int, prime_field: int,
                 generator: int, key: int):
        """
        Initialize the values here
        :param security_parameter: 1ⁿ
        :type security_parameter: int
        :param prime_field: q
        :type prime_field: int
        :param generator: g
        :type generator: int
        :param key: k
        :type key: int
        """
        pass

    def enc(self, message: int, random_seed: int) -> str:
        """
        Encrypt message against Chosen Plaintext Attack
        :param message: m
        :type message: int
        :param random_seed: r
        :type random_seed: int
        """
        pass

    def dec(self, cipher: str) -> int:
        """
        Decrypt ciphertext to obtain plaintext message
        :param cipher: ciphertext c
        :type cipher: str
        """
        pass
