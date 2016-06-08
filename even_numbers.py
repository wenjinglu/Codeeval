import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()

        if int(test) % 2 == 1:
            print '0'
        else:
            print '1'
