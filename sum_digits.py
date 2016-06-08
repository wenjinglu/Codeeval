import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        result = 0
        for i in test:
            result = result + int(i)
        print result
