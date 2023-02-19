import os, sys
from typing import Optional

parent = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath("_file_")), os.pardir))
sys.path.insert(0, parent)

from PRF.PRF import PRF

class CPA:
    def __init__(self, security_parameter: int, prime_field: int,
                 generator: int, key: int, mode="CTR"):
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
        :param mode: Block-Cipher mode of operation
            - CTR
            - OFB
        :type mode: str
        """
        self.security_parameter = security_parameter
        self.prime_field = prime_field
        self.generator = generator
        self.key = key
        self.mode = mode

    def enc(self, message: str, random_seed: int) -> str:
        """
        Encrypt message against Chosen Plaintext Attack using randomized ctr mode
        :param message: m
        :type message: int
        :param random_seed: ctr
        :type random_seed: int
        """
        block_size = self.security_parameter
        l = len(message)
        msg_blocks = []
        while l - block_size > 0:
            msg_blocks.append(message[l-block_size:l])
            l -= block_size
        if l > 0:
            msg_blocks.append(message[0:l].zfill(block_size))
        ciphertext = bin(random_seed)[2:].zfill(block_size)
        blck_no = 0
        msg_blocks = msg_blocks[::-1]
        curr_ciphertext = None
        for blck in msg_blocks:
            blck_no += 1
            if self.mode == "CTR":
                prf = PRF(self.security_parameter, self.generator, self.prime_field, self.key)
                Fkr = prf.evaluate(random_seed + blck_no)
                curr_ciphertext = str(bin(Fkr ^ int(blck, 2))[2:].zfill(block_size))
                ciphertext += curr_ciphertext

            elif self.mode == "OFB":
                prf = PRF(self.security_parameter, self.generator, self.prime_field, self.key)
                Fkr = 0
                if blck_no == 1:
                    Fkr = prf.evaluate(random_seed)
                else:
                    Fkr = prf.evaluate(Fkr)
                curr_ciphertext = str(bin(Fkr ^ int(blck, 2))[2:].zfill(block_size))
                ciphertext += curr_ciphertext

        return ciphertext
        

    def dec(self, cipher: str) -> str:
        """
        Decrypt ciphertext to obtain plaintext message
        :param cipher: ciphertext c
        :type cipher: str
        """
        block_size = self.security_parameter
        random_seed = int(cipher[:block_size], 2)

        l = block_size
        ciph_blocks = []
        msg = ""
        while l < len(cipher):
            ciph_blocks.append(cipher[l:l+block_size])
            l += block_size

        blck_no = 1

        for blck in ciph_blocks:
            if self.mode == "CTR":
                prf = PRF(self.security_parameter, self.generator, self.prime_field, self.key)
                Fkr = prf.evaluate(random_seed + blck_no)
                curr_msg = str(bin(Fkr ^ int(blck, 2))[2:].zfill(block_size))
                msg += curr_msg
            elif self.mode == "OFB":
                prf = PRF(self.security_parameter, self.generator, self.prime_field, self.key)
                Fkr = 0
                if blck_no == 1:
                    Fkr = prf.evaluate(random_seed)
                else:
                    Fkr = prf.evaluate(Fkr)
                curr_msg = str(bin(Fkr ^ int(blck, 2))[2:].zfill(block_size))
                msg += curr_msg
            blck_no += 1

        return msg


import csv
if __name__ == "__main__":
    flag = 0
    f = open('../IO/output/cpa.txt', 'r')
    out = f.readlines()
    with open('../IO/inputs/cpa.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        i = 0
        for lines in csvFile:
            if i > 0:
                lines = [int(val) for val in lines]
                n = lines[0] 
                p = lines[1]
                g = lines[2]
                k = lines[3]
                m = lines[4]
                r = lines[5]
                cpa = CPA(n, p, g, k, "CTR")
                cipher = cpa.enc(str(m), int(r))
                if cipher != out[i][:-1]:
                    flag = 1
                    print("Mismatch")
                dec = cpa.dec(cipher)
                if dec != str(m):
                    print("Faulty Decryption in CTR Mode!")

                cpa = CPA(n, p, g, k, "OFB")
                cipher = cpa.enc(str(m), int(r))
                dec = cpa.dec(cipher)
                if dec != str(m):
                    print("Faulty Enc-Decrypt in OFB mode!")
            i += 1
    if flag == 0:
        print("OK")