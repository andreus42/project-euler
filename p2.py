# p2: Even Fibonacci numbers
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# 8-5-2018, 8:55am-9:15am (20 minutes)

sum = 0
current_fib = 1
first_fib = 0
second_fib = 1

while current_fib < 4000000:
    current_fib = first_fib + second_fib
    first_fib = second_fib
    second_fib = current_fib
    if (current_fib%2==0):
        sum += current_fib

print(f'Sum: {sum}')
