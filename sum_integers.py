import sys

with open(sys.argv[1], 'r') as test_cases:
    result = 0
    for test in test_cases:
        result = result + int(test)
    print result
