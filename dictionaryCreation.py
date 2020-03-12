'''Python function which generates 
and returns a dictionary where the keys are numbers between 1 and n (both inclusive) and the values are square of keys.
if input is 10, then the output is to be {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
'''

def generate_dict(number):
	#start writing your code here
    new_dict={k:k**2 for k in range(1,number+1)}
    return new_dict

number=int(input())
print(generate_dict(number))
