'''Python function which accepts a string and returns a string made of the first 2 and the last 2 characters of the given string.
If the string length is less than 2, return -1.'''
def string_both_ends(input_string):
	#start writing your code here
    if len(input_string)<2:
        return -1
    elif len(input_string)==2:
        return input_string+input_string
    else:
        return input_string[:2]+input_string[-2:]
input_string=input()
print(string_both_ends(input_string))
