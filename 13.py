from itertools import combinations
N = int(input())
L =input().split()
K=int(input())
combos=list(combinations(range(N), K))
contains_a =[c for c in combos if any(L[i] =='a' for i in c)]
print(f"{len(contains_a)/len(combos):.4f}")
