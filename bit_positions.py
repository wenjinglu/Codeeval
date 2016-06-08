import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test_list = test.split(',')
        test_list = [int(i) for i in test_list]

        num = bin(test_list[0])[2:]
        if num[-test_list[1]] == num[-test_list[2]]:
            print 'true'
        else:
            print 'false'
