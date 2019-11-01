'''Python function which generates 
and returns a dictionary where the keys are numbers between 1 and n (both inclusive) and the values are square of keys.'''

def generate_dict(number):
	#start writing your code here
    new_dict={k:k**2 for k in range(1,number+1)}
    return new_dict

number=int(input())
print(generate_dict(number))
