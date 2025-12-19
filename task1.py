"""
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
"""

# def factorial(num):
#     factor = 1
#     while num>1:
#         factor*=num
#         num-=1
#     return factor
#
# n  = int(input("Enter the number : "))
# res = factorial(n)
# print(f"the factorial of {n} : {res}")


# USING RECURSION

def factorial(num):
    if num == 1:
        return 1
    else:
        fact_num = num * (factorial(num-1))
        return fact_num

n = int(input("Enter the number: "))
res = factorial(n)
print(f"the factorial of {n} : {factorial(n)}")
