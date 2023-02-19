import os, sys
from typing import Optional

parent = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath("_file_")), os.pardir))
sys.path.insert(0, parent)

from PRF.PRF import PRF

class MAC:
    def __init__(self, security_parameter: int, prime_field: int,
                 generator: int, seed: int):
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
        self.security_parameter = security_parameter
        self.prime_field = prime_field
        self.generator = generator
        self.seed = seed

    def mac(self, message: str, random_identifier: int) -> str:
        """
        Generate tag t
        :param random_identifier: r
        :type random_identifier: int
        :param message: message encoded as bit-string
        :type message: str
        """
        block_size = self.security_parameter // 4
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
        tag = bin(random_identifier)[2:].zfill(block_size)
        for blck in msg_blocks:
            blck_no += 1
            prf = PRF(self.security_parameter, self.generator, self.prime_field, self.seed)
            rdim = ""
            rdim += bin(random_identifier)[2:].zfill(block_size)
            rdim += bin(d)[2:].zfill(block_size)
            rdim += bin(blck_no)[2:].zfill(block_size)
            rdim += blck
            curr_tag = prf.evaluate(int(rdim, 2))
            tag += bin(curr_tag)[2:].zfill(block_size * 4)
        return tag

    def vrfy(self, message: str, tag: str) -> bool:
        """
        Verify whether the tag commits to the message
        :param message: m
        :type message: str
        :param tag: t
        :type tag: str
        """
        check = False
        block_size = self.security_parameter // 4
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
        random_identifier = int(tag[:block_size], 2)
        calc_tag = bin(random_identifier)[2:].zfill(block_size)
        for blck in msg_blocks:
            blck_no += 1
            prf = PRF(self.security_parameter, self.generator, self.prime_field, self.seed)
            rdim = ""
            rdim += bin(random_identifier)[2:].zfill(block_size)
            rdim += bin(d)[2:].zfill(block_size)
            rdim += bin(blck_no)[2:].zfill(block_size)
            rdim += blck
            curr_tag = prf.evaluate(int(rdim, 2))
            calc_tag += bin(curr_tag)[2:].zfill(block_size * 4)
        if calc_tag == tag:
            check = True
        return check



import csv
if __name__ == "__main__":
    flag = 0
    f = open('../IO/output/mac.txt', 'r')
    out = f.readlines()
    with open('../IO/inputs/mac.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        i = 0
        for lines in csvFile:
            if i > 0:
                n = int(lines[0])
                p = int(lines[1])
                g = int(lines[2])
                s = int(lines[3])
                m = lines[4]
                r = lines[5]
                mac = MAC(n, p, g, s)
                tag = mac.mac(m, int(r))
                if tag != out[i][:-1]:
                    print(tag, out[i][:-1], len(tag), len(out[i][:-1]))
                    flag = 1
                    print("Mismatch")
                check = mac.vrfy(m, tag)
                if check != 1:
                    print("Not verified!")
            i += 1
    if flag == 0:
        print("OK")