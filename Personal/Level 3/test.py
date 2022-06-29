from fractions import Fraction

def solution(m):
    for i in range (len(m)):
        m[i][i] = 0
    if sum(m[0]) == 0:
        return [1, 1]

    def gcd(a, b):
        if(b == 0):
            return a
        else:
            return gcd(b, a % b)


    def identityMatrix(length):
        I = []
        for i in range(length):
            cur = []
            for j in range(length):
                if j == i:
                    cur.append(1)
                else:
                    cur.append(0)
            I.append(cur)

        return I

    def return_transpose(mat):
        return list(map(list,zip(*mat)))

    def return_matrix_minor(mat,i,j):
        return [row[:j] + row[j+1:] for row in (mat[:i]+mat[i+1:])]

    def return_determinant(mat):
        if len(mat) == 2:
            return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]

        determinant = 0
        for c in range(len(mat)):
            determinant += ((-1)**c)*mat[0][c]*return_determinant(return_matrix_minor(mat,0,c))
        return determinant

    def inverse_matrix(m):
        if len(m) == 1:
            return [[1/m[0][0]]]

        determinant = return_determinant(m)
        if len(m) == 2:
            return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                    [-1*m[1][0]/determinant, m[0][0]/determinant]]

        cfs = []
        for r in range(len(m)):
            cfRow = []
            for c in range(len(m)):
                minor = return_matrix_minor(m,r,c)
                cfRow.append(((-1)**(r+c)) * return_determinant(minor))
            cfs.append(cfRow)
        cfs = return_transpose(cfs)
        for r in range(len(cfs)):
            for c in range(len(cfs)):
                cfs[r][c] = cfs[r][c]/determinant
        return cfs

    def matrix_multiply(X, Y, result):
        for i in range(len(X)):
            # iterate through columns of Y
            for j in range(len(Y[0])):
                # iterate through rows of Y
                for k in range(len(Y)):
                    result[i][j] += X[i][k] * Y[k][j]

        return result

    #m = [[Fraction(1, 1), Fraction(-1, 2)],[Fraction(-4, 9), Fraction(1, 1)]]
    #print(inverse_matrix(m))

    # SOLUTION STARTS HERE

    if m == [[0]]:
        return [1,1]

    n = len(m)

    #print(m)
    
    # Rearrange the so that the terminal states are on the bottom and the transient on top

    # Track the swaps so that we can convert back when returning the result
    # map[i] = j, where i is the ith state in the matrix and j is the original state that i corresponds to
    mapping = []
    for i in range(n):
        mapping.append(i)

    pointer = n - 1

    for i in range(n):
        # Completion Check
        if i >= pointer:
            break

        # If Terminal
        if sum(m[i]) == 0:
            # Bring pointer up until it isn't pointing to a terminal state
            flag = False
            while sum(m[pointer]) == 0:
                pointer -= 1 
                if i >= pointer:
                    flag = True
                    break
            if flag:
                break

            # Swap with array at pointer
            temp = m[pointer]
            m[pointer] = m[i]
            m[i] = temp

            # Adjust map
            temp = mapping[pointer]
            mapping[pointer] = mapping[i]
            mapping[i] = temp

            # Swap the ith and pointer terms in each array
            for j in range(n):
                temp = m[j][i]
                m[j][i] = m[j][pointer]
                m[j][pointer] = temp

            # Set pointer up by one row
            pointer -= 1

    #print(m)

    # Convert to fractions
    for i in range(len(m)):
        denominator = sum(m[i])
        if denominator != 0:
            for j in range(len(m[i])):
                m[i][j] = Fraction(m[i][j], denominator)

    #print(m)

    # Count num of terminal states
    t = 0
    for i in range(n):
        if sum(m[i]) == 0:
            t += 1

    if t == 1:
        return [1, 1]
    # Non-terminal states
    nt = n - t

    # FORMULA: N = (I-Q)**(-1)

    # Calculate I (Identity Matrix)
    I = identityMatrix(nt)

    # Calculate (I-Q)
    IminusQ = []
    for i in range(nt):
        cur = []
        for j in range(nt):
            cur.append(I[i][j] - m[i][j])
        IminusQ.append(cur)

    # Calculate N = (I-Q)**(-1)
    N = inverse_matrix(IminusQ)


    # FORMULA : B = NR

    R = []
    for i in range(nt):
        cur = []
        for j in range(nt, n):
            cur.append(m[i][j])
        R.append(cur)


    # B Dimensions are rows of N, columns of R, or nt rows & t columns
    result = []
    for i in range(nt):
        cur = []
        for j in range(t):
            cur.append(0)
        result.append(cur)

    B = matrix_multiply(N, R, result)


    ans = []
    for i in range(n):
        ans.append(-1)
    
    for i in range(len(B[0])):
        ans[mapping[nt+i]] = B[0][i]

    for i in reversed(range(len(ans))):
        if ans[i] == -1:
            del ans[i]

    denoms = []
    for i in range(len(ans)):
        denoms.append(ans[i].denominator)

    lcm = 1
    for i in denoms:
        lcm = lcm*i//gcd(lcm, i)

    for i in range(len(ans)):
        ans[i] = ans[i].numerator * (lcm // ans[i].denominator)
    ans.append(lcm)

    return ans

m = [
        [0,1,0,0,0,1],
        [4,0,0,3,2,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]
    ]

n = [
        [0, 2, 1, 0, 0], 
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0,0],
        [0, 0, 0, 0, 0]
    ]


# wrong
s = [
    [0, 0, 3, 0, 1],
    [0, 5, 2, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 4, 5, 0, 3],
    [0, 0, 0, 0, 0],
]



print(solution(s))
print(solution(m))
print(solution(n))
