# p4: Largest palindrome product
# What is the largest prime factor of the number 600851475143 ?
# https://projecteuler.net/problem=4
# 8-5-2018, 9:43pm-10:27pm

def is_palindrome(num):
    num_str=str(num)
    return num_str[::-1]==num_str

myList = []

for n in range(100,999):
    for x in range(100,999):
        myList.append(x*n)

answer = sorted(myList, reverse=True)

for num in answer:
    if is_palindrome(num):
        print(num)
        break
