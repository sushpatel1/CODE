from cidm6330.numToroman import NumeralsToRoman
import unittest

class NumToRomanTest(unittest.TestCase):
   def test_working(self):
       pass


   def NumToRomanTest(self):
       numeral = NumeralsToRoman(105)
       Expected_Val = "CV"
       Actual_val = numeral.NumToRoman()
       
       self.assertEqual(Expected_Val, Actual_val)
     

   def NumToRomanTest1(self):
       numeral = NumeralsToRoman(0)
       Expected_Val = "not a valid Number"
       Actual_val = numeral.NumToRoman()

       self.assertEqual(Expected_Val, Actual_val)