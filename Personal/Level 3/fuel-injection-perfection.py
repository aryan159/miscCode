import random

# I had lots of fun with this problem because it's deceptively simeple but gets tricky because of the constraints
# n has a max length of 309 digits, which may seem random at first 
# but len(str(2**1000)) = 302 {with python's recursion depth limit of 1000, we can only reliably solve numbers with 302 digits}

# So there are 2 solutions

# Solution 1: Optimize every tiny little thing to stay within the recursion limit

def solution(n):
    n = int(n)
    mem = {1:0}
    def re(n):
        if n in mem.keys():
            return mem[n]
        elif n % 2 == 1:

            # Add 1
            addOne = n + 1
            count = 0
            while addOne % 2 == 0:
                addOne = addOne // 2
                count += 1
            mem[addOne] = re(addOne)
            temp = addOne
            # Populate mem with values we skipped
            for i in range(1, count + 1):
                temp *= 2
                mem[temp] = mem[addOne] + i

            # Subtract 1
            minusOne = n - 1
            count = 0
            while minusOne % 2 == 0:
                minusOne = minusOne // 2
                count += 1
            mem[minusOne] = re(minusOne)
            temp = minusOne
            # Populate mem with values we skipped
            for i in range(1, count + 1):
                temp *= 2
                mem[temp] = mem[minusOne] + i

            return 1 + min(mem[n + 1], mem[n - 1])
        elif n % 2 == 0:
            print('SOMETHING VERY WRONG HAS HAPPENED')

    add = 0
    while n % 2 == 0:
        n = n // 2
        add += 1

    return add + re(n)



# Solution 2 [Bad Boy Solution]: Simply increase the Python recursion limit
# Google hates this solution so much that it won't even let me mention the function in the comments
# So let's just make our own pseudo call stack to get around this limit ;)


def solution(n):
    n = int(n)
    mem = {1:0}
    stack = []
    stack.append(n)
    while len(stack) > 0:
        cur = stack[-1]
        if cur in mem.keys():
            stack.pop()
        else:
            if cur % 2 == 0:
                if cur//2 not in mem.keys():
                    stack.append(cur//2)
                    continue
                mem[cur] = mem[cur//2] + 1
            elif cur % 2 == 1:
                if cur + 1 not in mem.keys():
                    stack.append(cur + 1)
                    continue

                if cur - 1 not in mem.keys():
                    stack.append(cur - 1)
                    continue

                mem[cur] = 1 + min(mem[cur+1], mem[cur-1])


    return mem[n]




def gen(n):
    ans = ''
    for i in range(n):
        ans += str(random.randint(0,9))
    return ans

print(solution(gen(300)))

