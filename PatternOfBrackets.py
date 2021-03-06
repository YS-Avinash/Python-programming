"""python function which accepts a string containing a pattern of brackets and returns true if the pattern of brackets is correct. Otherwise it returns false.
The string of brackets is correct if it satisfies the following conditions:
1. Number of opening and closing brackets are equal.
2. Pattern should not start with closing bracket and end with opening bracket."""

def bracket_pattern(input_str):
	if input_str.startswith(")") or input_str.endswith("(") :
	    result = False
	else :
	    count = 0
	    for paranthesis in input_str:
	        if paranthesis == "(":
	            count = count+1
	        else :
	            count = count-1
	    result = True if count == 0 else False
	return result
#Let input be "(())("
input_str = input()
print(bracket_pattern(input_str))
