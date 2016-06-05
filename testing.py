import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test_str, design_str = test.split('|')
        test_str = test_str.strip()
        design_str = design_str.strip()
        count = 0
        for i in range(len(test_str)):
            if test_str[i] != design_str[i]:
                count = count + 1
        if count == 0:
            print 'Done'
        elif count <= 2:
            print 'Low'
        elif count <=4:
            print 'Medium'
        elif count <= 6:
            print 'High'
        else:
            print 'Critical'
