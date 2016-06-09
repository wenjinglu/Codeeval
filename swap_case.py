import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.rstrip()
        result = []
        for i in test:
            if not i.isalpha():
                result.append(i)
            elif i.islower():
                result.append(i.upper())
            else:
                result.append(i.lower())
        print ''.join(result)
