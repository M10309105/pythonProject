#/usr/bin/python3
#
#Class
print("=" * 100)
print("10.11 Quality Control")
print("=" * 100)

#doctest
import doctest
def average(values):
    """
    This is average
    >>> print(average([1,2,3,4]))
    2.5
    """
    return sum(values) / len(values)

doctest.testmod()    

#comlated: unittest

import unittest
class TestFunctions(unittest.TestCase):
    def testAverage(self):
        self.assertEqual(average([10,20,30]),20)
        self.assertEqual(round(average([1,2,3]),1),2.0)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()