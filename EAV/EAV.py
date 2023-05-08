import os, sys
from typing import Optional

parent = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath("_file_")), os.pardir))
sys.path.insert(0, parent)

from PRG.PRG import PRG

class Eavesdrop:
    def __init__(self, security_parameter: int, key: int, expansion_factor: int,
                 generator: int, prime_field: int):
        """
        Initialize values here
        :param security_parameter: 1ⁿ
        :type security_parameter: int
        :param key: k, uniformly sampled key
        :type key: int
        :param expansion_factor: l(n)
        :type expansion_factor: int
        :param generator: g
        :type generator: int
        :param prime_field: p
        :type prime_field: int
        """
        self.security_parameter = security_parameter
        self.key = key
        self.expansion_factor = expansion_factor
        self.generator = generator
        self.prime_field = prime_field

    def enc(self, message: str) -> str:
        """
        Encrypt Message against Eavesdropper Adversary
        :param message: message encoded as bit-string
        :type message: str
        """
        prg = PRG(self.security_parameter, self.generator, self.prime_field, len(message))
        gk = prg.generate(self.key)
        return str(bin(int(gk, 2) ^ int(message, 2))[2:].zfill(len(message)))
        

    def dec(self, cipher: str) -> str:
        """
        Decipher ciphertext
        :param cipher: ciphertext encoded as bit-string
        :type cipher: str
        """
        prg = PRG(self.security_parameter, self.generator, self.prime_field, len(cipher))
        gk = prg.generate(self.key)
        return str(bin(int(cipher, 2) ^ int(gk, 2))[2:].zfill(len(cipher)))


import csv
if __name__ == "__main__":
    flag = 0
    f = open('../IO/output/eav.txt', 'r')
    out = f.readlines()
    with open('../IO/inputs/eav.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        i = 0
        for lines in csvFile:
            if i > 0:
                lines = [int(val) for val in lines]
                n = lines[0] 
                k = lines[1]
                ln = lines[2]
                g = lines[3]
                p = lines[4]
                m = lines[5]
                eav = Eavesdrop(n, k, ln, g, p)
                cipher = eav.enc(str(m))
                if cipher != out[i][:-1]:
                    flag = 1
                    print("Mismatch")
                dec = eav.dec(cipher)
                if dec != str(m):
                    print("Faulty Decryption!")
            i += 1
    if flag == 0:
        print("OK")
