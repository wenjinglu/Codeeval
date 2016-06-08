import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        lower = 0
        for i in test:
            if i.islower() :
                lower = lower + 1
        length = len(test)*1.0
        lower_ratio = (lower/length)*100
        upper_ratio = 100 - lower_ratio
        print "lowercase: %.2f uppercase: %.2f" %(lower_ratio, upper_ratio)
