'''
Understand:
input = string binary
output = string

Plan:
split string to individual letters in pieces of 8 bits
rejoin string together
'''

def csBinaryToASCII(binary):
  if len(binary) == 0:
    return binary
 n=8
bin_list = [binary[i:i+n] for i in range(0, len(binary), n)]
print(bin_list)
ret_string = ""

for bit in bin_list:
  ret_string += chr(int(bit, 2))
 
return ret_string

# print(bin_list)
# print(int(bin_list[0], 2))
# print(chr(int(bin_list[0], 2)))
