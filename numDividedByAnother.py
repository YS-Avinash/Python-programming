def check_numbers(num1,num2):
    lis=[n for n in range(num1,num2+1)]
    num_list=[]
    for i in range(1,len(lis)):
        new_lis=lis[:i]
        vals=list(filter(lambda x: lis[i]%x==0,new_lis))
        if not len(vals)==0:
            num_list.append(lis[i])
    count=len(num_list)
    return [set(num_list),count]

num1=10
num2=30
print(check_numbers(num1, num2))
