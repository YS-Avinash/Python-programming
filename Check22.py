'''
python function which accepts a list of numbers and returns true if the list contains a 2 next to a 2. Otherwise it should return false.
'''
def check_22(num_list):
    return "22" in "".join(map(str,num_list))    
print(check_22([3,2,5,1,2,1,2,2]))
