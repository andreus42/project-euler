import math

# is_prime v1 (don't change)
def is_prime(num):
    for n in range((num-1),1,-1):
        if num%n==0:
            return 0
    return 1


# is_prime v2
# def is_prime(num):
#     for n in range(2, (int(math.sqrt(num))), 2):
#         if num%n==0:
#             return 0
#         return 1

def product(list):
    p = 1
    for i in list:
        p *= i
    return p
