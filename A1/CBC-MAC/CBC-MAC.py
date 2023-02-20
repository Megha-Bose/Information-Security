import os, sys
from typing import Optional, List

parent = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath("_file_")), os.pardir))
sys.path.insert(0, parent)

from PRF.PRF import PRF

class CBC_MAC:
    def __init__(self, security_parameter: int, generator: int,
                 prime_field: int, keys: list):
        """
        Initialize the values here
        :param security_parameter: 1ⁿ
        :type security_parameter: int
        :param generator: g
        :type generator: int
        :param prime_field: q
        :type prime_field: int
        :param keys: k₁, k₂
        :type keys: list[int]
        """
        self.security_parameter = security_parameter
        self.generator = generator
        self.prime_field = prime_field
        self.keys = keys

    def mac(self, message: str) -> int:
        """
        Message Authentication code for message
        :param message: message encoded as bit-string m
        :type message: str
        """
        block_size = self.security_parameter
        l = len(message)
        msg_blocks = []
        i = 0
        d = 0
        while i + block_size < l:
            msg_blocks.append(message[i:i+block_size])
            i += block_size
            d += 1
        if i < l:
            msg = message[i:l]
            start = i
            end = i + block_size
            i = l
            while i < end:
                if i == l:
                    msg += "1"
                else:
                    msg += ("0"*(end-i))
                i += 1
            msg_blocks.append(msg)
            d += 1
        blck_no = 0
        initial = "0"*block_size
        curr_tag = int(initial, 2)
        for blck in msg_blocks:
            blck_no += 1
            prf = PRF(self.security_parameter, self.generator, self.prime_field, self.keys[0])
            inp = curr_tag ^ int(blck, 2)
            curr_tag = prf.evaluate(inp)
        prf = PRF(self.security_parameter, self.generator, self.prime_field, self.keys[1])
        final_tag = prf.evaluate(curr_tag)
        return final_tag

    def vrfy(self, message: str, tag: int) -> bool:
        """
        Verify if the tag commits to the message
        :param message: m
        :type message: str
        :param tag: t
        :type tag: int
        """
        return self.mac(message) == tag


import csv
if __name__ == "__main__":
    flag = 0
    f = open('../IO/output/cbc_mac.txt', 'r')
    out = f.readlines()
    with open('../IO/inputs/cbc_mac.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        i = 0
        for lines in csvFile:
            if i > 0:
                lines = [int(val) for val in lines]
                n = lines[0] 
                g = lines[1]
                p = lines[2]
                k1 = lines[3]
                k2 = lines[4]
                m = lines[5]
                cbc_mac = CBC_MAC(n, g, p, [k1, k2])
                tag = cbc_mac.mac(str(m))
                if str(tag) != out[i][:-1]:
                    flag = 1
                    print(tag, out[i][:-1])
                    print("Mismatch")
                check = cbc_mac.vrfy(str(m), tag)
                if check != 1:
                    print("Not verified!")
            i += 1
    if flag == 0:
        print("OK")