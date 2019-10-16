#Python function to add 'ing' at the end of a given string and return the new string.
#If the given string already ends with 'ing' then add 'ly'.
#If the length of the given string is less than 3, leave it unchanged.

def add_string(str1):
    return str1 if len(str1)<3 else str1+"ly" if str1.endswith("ing") else str1+"ing"

str1=input("Enter a string : ")
print(add_string(str1))
