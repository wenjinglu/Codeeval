import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test=test.replace(' ','')
        digit_sum = 0
        for i in range(1,17):
            if i % 2 == 0:
                digit_sum = digit_sum + int(test[i-1])
            else:
                digit_sum = digit_sum + int(test[i-1])*2
        if digit_sum % 10 == 0:
            print 'Real'
        else:
            print 'Fake'
