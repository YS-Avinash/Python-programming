'''Python function to rotate the list of elements by N positions. The function should return the rotated list.
Input list: [1, 2, 3, 4, 5, 6]
Number of positions to be rotated = 2
Output list: [5, 6, 1, 2, 3, 4]''''

def rotate_list(input_list,n):
    output_list = input_list[-n:]+input_list[:-n]
    return output_list

input_list= [1,2,3,4,5,6]
output_list=rotate_list(input_list,4)
print(output_list)
