L=None
def init(inp1,inp2):
    global L
    L = [[None]*(len(inp2)+1) for i in range(len(inp1)+1)] 

def lcs(inp1, inp2): 
	m = len(inp1) 
	n = len(inp2) 
	for i in range(m+1): 
		for j in range(n+1): 
			if i == 0 or j == 0 : 
				L[i][j] = 0
			elif inp1[i-1] == inp2[j-1]: 
				L[i][j] = L[i-1][j-1]+1
			else: 
				L[i][j] = max(L[i-1][j] , L[i][j-1])
				
def print_lcs(inp1,inp2):
    res=[]
    i=len(inp1)
    j=len(inp2)
    while i>0 and j>0:
        if inp1[i-1] == inp2[j-1]:
            res.append(inp1[i-1])
            i=i-1
            j=j-1
        elif L[i-1][j] > L[i][j-1]:
            i=i-1
        else:
            j=j-1
    print(*res[::-1],sep="")
            
x = input("Enter String 1:")
y = input("Enter String 2:")
init(x,y)
lcs(x,y)
print_lcs(x,y)
