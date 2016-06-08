import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.split()
        len_list = [len(i) for i in test]
        pos = len_list.index(max(len_list))
        print test[pos]
