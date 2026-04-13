You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.


#solution:
n= int(input())
nums =input().split()
print(all(int(i)> 0 for i in nums)and any(i == i[::-1] for i in nums))
