import sys
sys.path.append("..")   # append local PYTHONPATH
from ..sort.type import RandomType as rt
import random as rd

class Array:
    @staticmethod
    def generate(length, type):
        MAX = 10000
        if type == rt.Desc:
            return sorted([rd.randint(1, MAX) for _ in range(length)], reverse=True)
        elif type == rt.Asc:
            return sorted([rd.randint(1, MAX) for _ in range(length)])
        elif type == rt.Same:
            return [1] * length
        else:
            return [rd.randint(1, MAX) for _ in range(length)]