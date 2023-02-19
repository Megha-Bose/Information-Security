import os, sys
from typing import Optional

parent = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath("_file_")), os.pardir))
sys.path.insert(0, parent)

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
        self..key_cpa = key_cpa
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
        pass

    def dec(self, cipher: str) -> Optional[str]:
        """
        Decrypt ciphertext to obtain message
        :param cipher: <c, t>
        :type cipher: str
        """
        pass


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
                lines = [int(val) for val in lines]
                n = lines[0] 
                p = lines[1]
                g = lines[2]
                k_cpa = lines[3]
                k_mac1 = lines[4]
                k_mac2 = lines[5]
                m = lines[6]
                r = lines[7]
                cca = CCA(n, p, g, k_cpa, [k_mac1, k_mac2], "CTR")
                cipher = cca.enc(str(m), int(r))
                if cipher != out[i][:-1]:
                    flag = 1
                    print("Mismatch")
                dec = cca.dec(cipher)
                if dec != str(m):
                    print("Faulty Decryption in CTR Mode!")

                cca = CCA(n, p, g, k_cpa, [k_mac1, k_mac2], "OFB")
                cipher = cca.enc(str(m), int(r))
                dec = cca.dec(cipher)
                if dec != str(m):
                    print("Faulty Enc-Decrypt in OFB mode!")
            i += 1
    if flag == 0:
        print("OK")