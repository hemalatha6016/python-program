#You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.


def check_subset():
    t=int(input())  
    for _ in range(t):
        n=int(input())
        A=set(map(int, input().split()))       
        m=int(input())
        B=set(map(int, input().split()))      
        print(A.issubset(B))
check_subset()