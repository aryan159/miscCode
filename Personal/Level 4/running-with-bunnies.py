import itertools

def solution(times, time_limit):
    # First, we run Floyd-Warshall to determine minimum distances between each pair of nodes
    # We check for the presence of negative cycles by trying to find M[i][i] < 0 (distance to self is neg)

    # Then, we try to construct paths, starting from the most number of bunnies
    # We try every permutation starting from the lowest worker IDs and return when we find one

    # Floyd-Warshall
    for k in range(len(times)):
        for i in range(len(times)):
            for j in range(len(times)):
                times[i][j] = min(times[i][j], times[i][k] + times[k][j])

    # Detect Negative Cycles
    for i in range(len(times)):
        if times[i][i] < 0:
            return [i for i in range(0, len(times)-2)]

    # Generate permutations starting from the greatest size
    accepted_perms = []
    for perm_size in reversed(range(1, len(times) - 1)):
        foundSolution = False
        for perm in itertools.permutations(range(1, len(times) - 1), perm_size):
            perm = list(perm)
            perm = [0] + perm
            perm.append(len(times) - 1)

            # Find out cost of current perm
            current_cost = 0
            for i in range(1, len(perm)):
                current_cost += times[perm[i-1]][perm[i]]
            if current_cost <= time_limit:
                accepted_perms.append(perm)
                foundSolution = True
        if foundSolution:
            break

    # Find out which perm was lexographically smallest
    for i in range(len(accepted_perms)):
        accepted_perms[i].sort()

    ans = min(accepted_perms)
    ans.pop(0)
    ans.pop(-1)
    return [i-1 for i in ans]

print(solution([
    [0, 2, 2, 2, -1], 
    [9, 0, 2, 2, -1], 
    [9, 3, 0, 2, -1], 
    [9, 3, 2, 0, -1], 
    [9, 3, 2, 2, 0]], 
1))


print(solution([
    [0, 1, 1, 1, 1], 
    [1, 0, 1, 1, 1], 
    [1, 1, 0, 1, 1], 
    [1, 1, 1, 0, 1], 
    [1, 1, 1, 1, 0]], 
3))

print(solution([
    [0, -1, 89, 99, 99],
    [-1, 0, 93, 89, 38],
    [99, 48, 0, 23, 92],
    [78, 89, 88, 0, 68],
    [96, 56, 48, 56, 0]], 
5))