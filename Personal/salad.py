import binascii
from matplotlib import pyplot as plt
import numpy as np

def split(word):
    return [int(char) for char in word]

b = bin(int("7F7569FC", 16))
print(b)

num = "00000000,7F7569FC,4172BD04,5D5AA574,5D681574,5D021974,414CAD04,7F5555FC,00266400,670B2CBC,667612E0,3DCCA544,0A1BB7EC,0716EC18,5CC1BBF4,07538794,603422E0,5F6E4224,66A5F6E4,0799B3D4,1C2ABEE8,6736AFD0,0070AC58,7F2CC564,4144EC4C,5D7EBFCC,5D2592B8,5D39EE2C,416E202C,7F4E75E8,00000000,00000000"

nums = num.split(",")
lst=[]
for num in nums:
    lst.append(split(bin(int(num, 16))[2:].zfill(32)))

for i in lst:
    print(len(i))

g = np.array(lst, dtype=int)
np.set_printoptions(threshold=np.inf)

print(g)
# plt.subplot(211)
plt.imshow(g)
# plt.subplot(212)
plt.imshow(g, cmap='Greys',  interpolation='nearest')
plt.savefig('blkwht.png')

plt.show()

