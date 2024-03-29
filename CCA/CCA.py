from __future__ import annotations
import os, sys
from typing import Optional

import math

parent = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath("_file_")), os.pardir))
sys.path.insert(0, parent)

from CPA.CPA import CPA
from CBC_MAC.CBC_MAC import CBC_MAC

class CCA:
    def __init__(self, security_parameter: int, prime_field: int,
                 generator: int, key_cpa: int, key_mac: list[int],
                 cpa_mode="CTR"):
        """
        Initialize the values here
        :param security_parameter: 1ⁿ
        :type security_parameter: int
        :param prime_field: q
        :type prime_field: int
        :param generator: g
        :type generator: int
        :param key_cpa: k1
        :type key_cpa: int
        :param key_mac: k2
        :type key_mac: list[int]
        :param cpa_mode: Block-Cipher mode of operation for CPA
            - CTR
            - OFB
        :type cpa_mode: str
        """
        self.security_parameter = security_parameter
        self.prime_field = prime_field
        self.generator = generator
        self.key_cpa = key_cpa
        self.key_mac = key_mac
        self.cpa_mode = cpa_mode

    def enc(self, message: str, cpa_random_seed: int) -> str:
        """
        Encrypt message against Chosen Ciphertext Attack
        :param message: m
        :type message: str
        :param cpa_random_seed: random seed for CPA encryption
        :type cpa_random_seed: int
        """
        cpa = CPA(self.security_parameter, self.prime_field, self.generator, self.key_cpa, self.cpa_mode)
        cipher = cpa.enc(message, cpa_random_seed)
        cbc_mac = CBC_MAC(self.security_parameter, self.generator, self.prime_field, self.key_mac)
        tag = cbc_mac.mac(cipher)
        return cipher + bin(tag)[2:].zfill(self.security_parameter)

    def dec(self, cipher: str) -> Optional[str]:
        """
        Decrypt ciphertext to obtain message
        :param cipher: <c, t>
        :type cipher: str
        """
        cbc_mac = CBC_MAC(self.security_parameter, self.generator, self.prime_field, self.key_mac)
        tag = int(cipher[-self.security_parameter:], 2)
        c = cipher[:-self.security_parameter]
        check = cbc_mac.vrfy(c, tag)
        if check:
            cpa = CPA(self.security_parameter, self.prime_field, self.generator, self.key_cpa, self.cpa_mode)
            message = cpa.dec(c)
            return message


import csv
if __name__ == "__main__":
    flag = 0
    f = open('../IO/output/cca.txt', 'r')
    out = f.readlines()
    with open('../IO/inputs/cca.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        i = 0
        for lines in csvFile:
            if i > 0:
                n = int(lines[0]) 
                p = int(lines[1])
                g = int(lines[2])
                k_cpa = int(lines[3])
                k_mac1 = int(lines[4])
                k_mac2 = int(lines[5])
                m = lines[6]
                r = lines[7]
                cca = CCA(n, p, g, k_cpa, [k_mac1, k_mac2], "CTR")
                cipher = cca.enc(str(m), int(r))
                if cipher != str(out[i][:-1]):
                    flag = 1
                    print(n)
                    print(cipher)
                    print(str(out[i][:-1]))
                    print("Mismatch")
            i += 1
    if flag == 0:
        print("OK")