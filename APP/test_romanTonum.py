from cidm6330.romanTonum import RomanToNumerals
import unittest

class RomanToNumTest(unittest.TestCase):
   def test_working(self):
       pass

   def RomanToNumTest(self):
       numeral = RomanToNumerals("V")
       Expected_Val = 5
       Actual_val = numeral.RomanToNum()       
       self.assertEqual(Expected_Val, Actual_val)

   def RomanToNumTest1(self):
       numeral = RomanToNumerals("ABD")
       Expected_Val = "Numeral value is not valid"
       Actual_val = numeral.RomanToNum()
       
       self.assertEqual(Expected_Val, Actual_val)
      
