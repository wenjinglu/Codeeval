import sys

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        fib = [0,1]
        for i in range(2,n+1):
            fib.append(fib[i-1]+fib[i-2])
        return fib[n]


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print fibonacci(int(test))
