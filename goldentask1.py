from difflib import SequenceMatcher
  

string1 = input('Enter string 1:')
string2 = input('Enter string 2:')
  
# Using the SequenceMatcher()
match = SequenceMatcher(None,string1, string2)
  
# convert above output into ratio , multiply by 100

result = match.ratio() * 100
  
# Display the final result
print(int(result), "%")
