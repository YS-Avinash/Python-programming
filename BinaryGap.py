"""A binary gap within a positive integer N is any maximal sequence of consecutive zeros
that is surrounded by ones at both ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
The number 20 has binary representation 10100 and contains one binary gap of length 1.
The number 15 has binary representation 1111 and has no binary gaps.
The number 32 has binary representation 100000 and has no binary gaps."""

def binaryGap(N):
        binary_value = bin(N)[2:]
        values = [int(digit) for digit in binary_value]
        ones=[pos for pos in range(len(values)) if values[pos]==1]
        maxi=-1
        for i in range(1,len(ones)):
              val=ones[i]-ones[i-1]
              if val>maxi:
                      maxi=val
        return maxi-1 if maxi>-1 else 0
print(binaryGap(1041))
