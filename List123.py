"""A python function which accepts a list of numbers and returns true, if 1, 2, 3 appears in sequence in the list.
Otherwise, it should return false."""


def list123(nums):
    #start writing your code here
    val = "".join(map(str,nums))
    return "123" in val
#Let nums input be [1,2,3,4,5]
nums = eval(input())
print(list123(nums))
