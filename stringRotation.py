'''
Input:- 
	rhdt:246,ghftd:1246
Output: 
	trhd,ftdgh
Explanation:-
	 Here,every string(rhdt:1246) is associated with a number ,separated by semicolon, if sum of squares of digits is even then rotate the string right by 1 position. If sum of squares of digit is odd then rotate the string left by 2 positions.
2*2+4*4+6*6=84 which is even so rotate string right by 1 so "rhdt" will be "trhd"
For second case : 1*1+2*2+4*4+6*6=85 which is odd so rotate string left by 2 so "ghftd" will be "ftdgh"'''



from functools import reduce
sub=[i.split(':') for i in input().split(",")]
ls=[]
for val in sub:
    string=val[0]
    num=list(map(int,val[1]))
    res_sum=reduce(lambda x,y:x*x+y*y,num)
    if res_sum%2==0:
        string=string[-1]+string[:-1]
    else:
        string=string[2:]+string[:2]
    ls.append(string)
print(*ls,sep=",") 
