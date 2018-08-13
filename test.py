import time
start = time.time()

def judprime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        else:
            return True


def sumprime(m):
    return sum((x for x in range(m) if judprime(x)))


print(sumprime(2000000))

print(f'Answer of problem 10: {sumprime} in {time.time()-start} second(s)')
