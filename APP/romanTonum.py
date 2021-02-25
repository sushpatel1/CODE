class RomanToNumerals:
   

     def __init__(self, numeral):
       self.numeral = numeral

     def __str__(self) -> str:
        num = self.RomanToNum()
        return f"{num}"

     def __repr__(self) -> str:
        num = self.RomanToNum()
        return f"{num}"

    
     def RomanToNum(self):
       numeral = self.numeral
       dict = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, }

       number = 0
       i = 0
       for i in range(len(numeral)):
         if numeral[i] not in dict.keys():   
           return "Numeral value is not valid"
         
         current_numeral = dict[numeral[i]]             
         if (i+1 < len(numeral)): 
           Next_Numeral = dict[numeral[i+1]]
           if (current_numeral >= Next_Numeral): 
            number = number + current_numeral           
           else: 
             number = number - current_numeral 
         else: 
             number = number + current_numeral       
         
       return number
 