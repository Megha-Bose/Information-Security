from typing import Optional


class MAC:
    def __init__(self, security_parameter: int, prime_field: int,
                 generator: int,
                 seed: int):
        """
        Initialize the values here
        :param security_parameter: 1ⁿ
        :type security_parameter: int
        :param prime_field: q
        :type prime_field: int
        :param generator: g
        :type generator: int
        :param seed: k
        :type seed: int
        """
        pass

    def mac(self, message: str, random_identifier: int) -> int:
        """
        Generate tag t
        :param random_identifier: r
        :type random_identifier: int
        :param message: message encoded as bit-string
        :type message: str
        """
        pass

    def vrfy(self, message: str, tag: int) -> bool:
        """
        Verify whether the tag commits to the message
        :param message: m
        :type message: str
        :param tag: t
        :type tag: int
        """
        pass
