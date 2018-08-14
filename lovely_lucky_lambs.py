# p2: Even Fibonacci numbers
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# 8-5-2018, 8:55am-9:15am (20 minutes)

sum1 = 0
current_fib = 1
first_fib = 0
second_fib = 1
lambs = 10
print(current_fib)

print('Stingy')
while sum1 < lambs:
    current_fib = first_fib + second_fib
    print(current_fib)
    first_fib = second_fib
    second_fib = current_fib
    sum1 += current_fib

# Generous Scenario
print('Generous')
sum2 = 1

while (sum2) < lambs:
    print(sum2)
    sum2 = sum2*2


# answer
print (f'sum1: {sum1}\nsum2: {sum2}\nanswer: {sum2 - sum1}')

# testing
# while current_fib < 100:
#     current_fib = first_fib + second_fib
#     print(current_fib)
#     first_fib = second_fib
#     second_fib = current_fib
#     print(f'Diff {current_fib - second_fib}')
