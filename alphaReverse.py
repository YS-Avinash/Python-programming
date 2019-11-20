Given a input string contains alphabets and special symbbols,without changing the positions of special symbols reverse all the alphabets in
the string and reprint the string.For example ,if the input is a$^bcDs#n then the resultant output is n$^sDcb#a


'''st=list(input())
i,j=0,len(st)-1
while i<j:
    while not st[i].isalpha():
        i=i+1
    while not st[j].isalpha():
        j=j-1
    st[i],st[j]=st[j],st[i]
    i=i+1
    j=j-1
print("".join(st))'''
                        or    
'''st=list(input())
st_alpha=list(filter(lambda x:x.isalpha(),st))
st_alpha=st_alpha[::-1]
for i in range(len(st)):
    if st[i].isalpha():
        st[i]=st_alpha.pop(0)
print("".join(st))'''
