'''
Understand
Input: integer (n) Output: integer
integer -> binary -> reserve binary -> decimal
417 -> 110100001 -> 100001011 -> 267

Plan
for x in n
convert to binary
reserve 
convert to decimal

Execute
'''

def csReverseIntegerBits(n):
    return int(bin(n)[:1:-1],2)


#def csReverseIntegerBits(n):
    #if x in n: 
        #result = {0:b}.format(n)
        #int(str(x)[::-1])
        #int('n', 2)
    #print(result)
