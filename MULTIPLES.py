import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test_list = test.split(',')
        test_list = [int(i) for i in test_list]

        if test_list[0] % test_list[1] == 0:
            print test_list[0]
        else:
            print (1+test_list[0]/test_list[1])*test_list[1]
