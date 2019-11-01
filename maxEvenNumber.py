'''Read a string input,identify the maximum even number formed from the digits in string '''

inpt = set([i for i in input() if i.isdigit()]) 
max_number = sorted(inpt,reverse=True)
even_nums_in_list = [i for i in max_number if  int(i)%2==0]
if even_nums_in_list != []:
    min_even = min(even_nums_in_list)
    max_number.remove(min_even)
    max_number.append(min_even)
    print(*max_number,sep="")
else:
    print(-1)
