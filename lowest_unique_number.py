import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test_list = test.split()
        test_list = [int(i) for i in test_list]
        num_dict = {}
        for item in test_list:
            if item in num_dict:
                num_dict[item] = num_dict[item] + 1
            else:
                num_dict[item] = 1
        result = []
        for key,value in num_dict.iteritems():
            if value == 1:
                result.append(key)
        if len(result) == 0:
            print '0'
        else:
            print test_list.index(sorted(result)[0])+1
