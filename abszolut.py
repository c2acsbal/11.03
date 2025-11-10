import unittest

szam1 = int(input("Input: "))
szam2 = int(input())

def abs_max(szam1: int, szam2: int):
    if szam1 < 0:
        szam1 *= -1
    elif szam2 < 0:
        szam2 *= -1

    if szam1 > szam2:
        return szam1
    else:
        return szam2
    
class TesztAbszolut(unittest.TestCase):
    def test_elso_eset(self):
        veg = abs_max(-5,1)
        self.assertEqual(veg, 5)
print(f"Retrun: {abs_max(szam1, szam2)}")

unittest.main()