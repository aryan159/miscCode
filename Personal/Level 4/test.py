import itertools

l = [1,1,3,4]
print(itertools.permutations(range(4)))

for perm in itertools.permutations(l):
    print(perm)