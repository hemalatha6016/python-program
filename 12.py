Goal: Print a numerical palindrome triangle of size
using math only (no strings) and only one line inside the loop.


for i in range(1, int(input()) + 1):
    print(((10**i - 1) // 9)**2)
