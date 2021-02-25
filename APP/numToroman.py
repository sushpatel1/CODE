class NumeralsToRoman:
   

     def __init__(self, number):
       self.number = number

     def __str__(self) -> str:
        roman = self.NumToRoman()
        return f"{roman}"

     def __repr__(self) -> str:
        roman = self.NumToRoman()
        return f"{roman}"

    
     def NumToRoman(self):
       Number = self.number
       dict = { 1000:"M", 900:"CM", 500:"D", 400:"CD",
                100:"C", 90:"XC", 50:"L", 40:"XL",
                10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I" }

       roman_number = ''
       i = 0
       if Number <= 0:
         return "not a valid Number"

       while  Number > 0 and Number <= 3000:
           for k, v in dict.items():
            while Number >= k:
                roman_number += v
                Number -= k
       return roman_number







            






