Apply your knowledge of the .add() operation to help your friend Rupal.
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.
Find the total number of distinct country stamps.


PROGRAM:

def count_distinct_stamps():
    n=int(input())
    stamps=set() 
    for _ in range(n):
        country=input().strip()
        stamps.add(country)
    print(len(stamps))
count_distinct_stamps()
