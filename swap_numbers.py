import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test_list = test.split()
        result = []
        for item in test_list:
            result.append(item[-1:] + item[1:-1] + item[:1])
        print ' '.join(result)
