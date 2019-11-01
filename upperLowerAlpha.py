'''Find count of caps and small letters in a string '''

def find_upper_and_lower(sentence):
    #start writing your code here
    result_list=[]
    result_list.append(len([" " for i in sentence if i.isupper()]))
    result_list.append(len([" " for i in sentence if i.islower()]))
    return result_list
sentence=input()
print(find_upper_and_lower(sentence))
