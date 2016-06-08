import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test_list = test.split()
        test_list = [float(i) for i in test_list]
        test_list = sorted(test_list)
        test_list = ['{0:.3f}'.format(i) for i in test_list]
        print ' '.join(test_list)
