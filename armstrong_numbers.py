import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        #test_list = [int(i) for i in test]
        power_list = [int(i)**len(test) for i in test]
        if sum(power_list) == int(test):
            print 'True'
        else:
            print 'False'
