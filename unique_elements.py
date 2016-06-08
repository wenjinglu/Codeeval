#import sys
#import numpy

#with open(sys.argv[1], 'r') as test_cases:
#    for test in test_cases:
#        test = test.split(',')
#        test = [int(i) for i in test]
#        result = numpy.unique(test).tolist()
#        print str(result)[1:-1]

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.split(',')
        test = [int(i) for i in test]
        result = []
        for j in test:
            if j not in result:
                result.append(j)
        print ','.join([str(i) for i in result])
