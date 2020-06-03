'''python function which accepts three numbers and returns True if
a. one of the three numbers is "close" to any one of the other numbers (differing from a number by at most 1), and

b.Number that is left out is "far", differing from both other values by 2 or more.

Return false if the above mentioned conditions are not satisfied.'''
def close_number(num1,num2,num3):
    res=False
    lis=[num1,num2,num3]
    lis.sort()
    (num1,num2,num3) = lis
    if num3-num2<=1 and (num2-num1>=2 and num3-num1>=2):
        res=True
    elif num2-num1<=1 and (num3-num1>=2 and num3-num2>=2):
        res = True
    return res
print(close_number(5,4,2))
