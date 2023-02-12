from typing import Optional


class CBC_MAC:
    def __init__(self, security_parameter: int, generator: int,
                 prime_field: int, expansion_factor: int, keys: list[int]):
        """
        Initialize the values here
        :param security_parameter: 1ⁿ
        :type security_parameter: int
        :param generator: g
        :type generator: int
        :param prime_field: q
        :type prime_field: int
        :param expansion_factor: l(n)
        :type expansion_factor: int
        :param keys: k₁, k₂
        :type keys: list[int]
        """
        pass

    def mac(self, message: str) -> int:
        """
        Message Authentication code for message
        :param message: m (with length l(n).n)
        :type message: str
        """
        pass

    def vrfy(self, message: str, tag: int) -> bool:
        """
        Verify if the tag commits to the message
        :param message: m
        :type message: str
        :param tag: t
        :type tag: int
        """
        pass
