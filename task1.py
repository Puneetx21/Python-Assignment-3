# WITHOUT RECURSION


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


while True :
    n = int(input("Enter the number: "))
    res = factorial(n)
    print(f"the factorial of {n} : {factorial(n)}")
