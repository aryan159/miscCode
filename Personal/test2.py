with open("hash.txt","r") as f:
    file = f.read()
for i in range(25):
    print('[' + str(i+1) + ']' + file[i*64:i*64+64])