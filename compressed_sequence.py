import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test_list = test.split()
        test_list = [int(i) for i in test_list]
        num_dict = {}
        for i in test_list:
            if i in num_dict:
                num_dict[i] = num_dict[i] + 1
            else:
                num_dict[i] = 1
        result = []
        for key,value in num_dict.iteritems():
            result.append(value)
            result.append(key)
        result = [str(i) for i in result]
        print ' '.join(result)
