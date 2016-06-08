import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test_list = test.split()
        result = []
        for i in test_list:
            item = list(i)
            item[0] = item[0].upper()
            result.append(''.join(item))
        print ' '.join(result)
