import os, sys
from typing import Optional

parent = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath("_file_")), os.pardir))
sys.path.insert(0, parent)

from PRG.PRG import PRG

class PRF:
    def __init__(self, security_parameter: int, generator: int,
                 prime_field: int, key: int):
        """
        Initialize values here
        :param security_parameter: 1ⁿ
        :type security_parameter: int
        :param generator: g
        :type generator: int
        :param prime_field: p
        :type prime_field: int
        :param key: k, uniformly sampled key
        :type key: int
        """
        if security_parameter > 32:
            raise ValueError("security_parameter must be 32 or less")
        self.security_parameter = security_parameter
        self.generator = generator
        self.prime_field = prime_field
        self.key = key
        

    def evaluate(self, x: int) -> int:
        """
        Evaluate the pseudo-random function at `x`
        :param x: input for Fₖ
        :type x: int
        """
        res = self.key
        prg = PRG(self.security_parameter, self.generator, self.prime_field, 2 * self.security_parameter)
        for i in range(self.security_parameter):
            res = prg.generate(res)
            side = x & (1 << (self.security_parameter - i - 1))
            if side == 0:
                res = res[:self.security_parameter]
            else:
                res = res[self.security_parameter:]
            res = int(res, 2)
            # print(res)
        return res

        
import csv
if __name__ == "__main__":
    flag = 0
    f = open('../IO/output/prf.txt', 'r')
    out = f.readlines()
    with open('../IO/inputs/prf.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        i = 0
        for lines in csvFile:
            if i > 0:
                lines = [int(val) for val in lines]
                n = lines[0] 
                p = lines[1]
                g = lines[2]
                k = lines[3]
                s = lines[4]
                prf = PRF(n, g, p, k)
                o = prf.evaluate(s)
                if(o != int(out[i-1][:-1])):
                    flag = 1
                    print("Mismatch")
            i += 1
    if flag == 0:
        print("OK")