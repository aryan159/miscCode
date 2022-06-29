# This Python file uses the following encoding: utf-8
encoded_flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽'

def program(flag):
    return ''.join(
    [chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]
    )

def reverse(encoded_flag):
    # encoded_flag[i] = 2^8 * flag[2i] + flag[2i + 1]
    # flag values are lesser than 2^8
    # thus, flag[2i] = encoded_flag[i] // 2^8
    # flag[2i + 1] = encoded_flag[i] mod 2^8
    flag = ''
    for i in range(0, len(encoded_flag)):
        flag += chr(ord(encoded_flag[i]) // 2**8)
        flag += chr(ord(encoded_flag[i]) % 2**8)
    return flag

print(reverse(encoded_flag))