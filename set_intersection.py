import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        test_list = test.split(';')
        test_sub1 = test_list[0].split(',')
        test_sub2 = test_list[1].split(',')
        result = []
        for i in test_sub2:
            if i in test_sub1:
                result.append(i)
        print ','.join(result)
