'''
python function to print the given number of diagonal lines of stars.
Sample input: 5

Expected output will be:
*
**
***
****
*****
'''
def diagonal_stars(number):
   for _ in range(number):
       print("*"*_)
number=int(input())   
diagonal_stars(number)
