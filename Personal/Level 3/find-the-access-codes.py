import random

# Not fast enough O[N^3]
def solution1(l):
    ans = 0
    for i in range(len(l)-2):
        for j in range(i+1, len(l)-1):
            if l[j] % l[i] == 0:
                for k in range(j+1, len(l)):
                    if l[k] % l[j] == 0:
                        ans += 1
    return ans

def solution(l):
    count = []
    ans = 0
    for i in range (len(l)):
        count.append(0)
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                count[i] += 1

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                ans += count[j]

    return(ans)
    

def gen(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(1, 999999))
    return arr


print(solution([1,2,3,4,5,6]))
print(solution1([1,2,4,8,16,32,64,128, 256, 512, 1024, 2048, 2048]))