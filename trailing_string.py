import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        script = test.split(',')
        result = 1
        if len(script) > 0:
            n = len(script[0])-1
            for character in reversed(script[1].rstrip()):
                if character != script[0][n]:
                    result = 0
                n = n - 1
        print result
