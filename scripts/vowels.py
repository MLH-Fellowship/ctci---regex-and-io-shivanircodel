# Write the solution for "Filter Vowels".
import re 
import os 
from string import * 

print ("opening file")

pattern = "(a|e|i|o|u|A|E|I|O|U)"

with open ('vowels.txt','r') as f: 
  context = f.read()
  number_of_vowels = len(re.findall(pattern, context))
  print(number_of_vowels)
  string = str(number_of_vowels)
  os.rename("vowels.txt", "vowels-"+string+".txt")
