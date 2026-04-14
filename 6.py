#Read four integers a, b, c, and d, each on a separate line.
Print the value of a raised to the power b plus c raised to the power d.


def large_power_sum():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())    
    result=pow(a,b)+pow(c,d)
    print(result)
large_power_sum()