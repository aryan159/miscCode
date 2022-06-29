def solution(h, q):
    arr = ['0th Element']
    looseleafs = ['0th Element']
    for i in range(h):
        arr.append([])
        looseleafs.append(0)

    current = h
    for i in range(1, 2**h):
        arr[current].append(i)
        looseleafs[current] += 1
        if looseleafs[current] == 2:
            looseleafs[current] = 0
            current -= 1
        else:
            current = h

    ans = []
    for i in q:
        for j in range(1, h+1):
            if (arr[j].count(i) == 1):
                if (j == 1):
                    ans.append(-1)
                    break
                else:
                    index = (int)(arr[j].index(i)/2)
                    ans.append(arr[j-1][index])
                    break

    return ans

def display(arr):
    for innarr in arr:
        print(innarr)

print(solution(5, [19,14,28]))
            
    
    

    