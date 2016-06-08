import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        test_list = test.split(',')
        string = test_list[0]
        char = test_list[1]
        pos = len(string) - 1
        for i in reversed(string):
            if i == char:
                break
            else:
                pos = pos -1
        print pos
