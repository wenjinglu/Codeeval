import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        test = test.split(',')
        test = [int(i) for i in test]
        result = test[0] % test[1]
        print result
