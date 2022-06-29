def solution(x, y):
    dic = {}
    for i in x:
        if i not in dic:
            dic[i] = 0
        dic[i] += 1

    for i in y:
        # When y is bigger
        if i not in dic:
            return i
        dic[i] -= 1
        if dic[i] == 0:
            del dic[i]

    # When x is bigger
    for key in dic.keys():
        return key

x = [14, 27, 1, 4, 2, 50, 3, 1]
y = [2, 4, -4, 3, 1, 1, 14, 27, 50]


print(solution(x,y))