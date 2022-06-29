def solution(x, y):
    # 1 + 2 + 3 + ... + n = (1 + n)/2 * n

    # First find (x+y-1, 1)
    bottomIndex = x + y - 1
    curr = ((1 + bottomIndex) * bottomIndex) // 2

    # Then move diagonally up and left to get to (x, y)
    curr = curr - (y - 1)

    return str(curr)

print(solution(1, 1))