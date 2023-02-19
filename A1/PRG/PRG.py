import os, sys
from typing import Optional

parent = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath("_file_")), os.pardir))
sys.path.insert(0, parent)

class PRG:
    def __init__(self, security_parameter: int, generator: int,
                 prime_field: int, expansion_factor: int):
        """
        Initializing values
        :param security_parameter: n (from 1ⁿ)
        :type security_parameter: int
        :param generator: g
        :type generator: int
        :param prime_field: p
        :type prime_field: int
        :param expansion_factor: l(n)
        :type expansion_factor: int
        """
        if security_parameter > 32:
            raise ValueError("security_parameter must be 32 or less")
        self.security_parameter = security_parameter
        self.generator = generator
        self.prime_field = prime_field
        self.expansion_factor = expansion_factor

    def generate(self, seed: int) -> str:
        """
        Generate the pseudo-random bit-string from `seed`
        :param seed: uniformly sampled seed
        :type seed: int
        """
        typ = "DLP"
        owf_out = 0
        hcp = "0"
        generated_bit_string = ''
        x = seed
        for i in range(self.expansion_factor):
            if typ == "DLP":
                # DLP: g^x mod p
                mod_pow = pow(self.generator, x, self.prime_field)
                # Calculate msb of current x and append it to generated bit string.
                # Consider msb(x) = 0 if x < (p-1) / 2 else 1
                msb = "0" if x < ((self.prime_field - 1)/2) else "1"
                owf_out, hcp = mod_pow, msb
            generated_bit_string += hcp
            # Consider g^x as next x.
            x = owf_out
        return generated_bit_string


import csv
if __name__ == "__main__":
    flag = 0
    f = open('../IO/output/prg.txt', 'r')
    out = f.readlines()
    with open('../IO/inputs/prg.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        i = 0
        for lines in csvFile:
            if i > 0:
                lines = [int(val) for val in lines]
                n = lines[0] 
                g = lines[1]
                p = lines[2]
                ln = lines[3]
                s = lines[4]
                prg = PRG(n, g, p, ln)
                o = prg.generate(s)
                if(o != out[i-1][:-1]):
                    flag = 1
                    print("Mismatch")
            i += 1
    if flag == 0:
        print("OK")