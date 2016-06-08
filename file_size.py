import sys
#import os

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print sys.getsizeof(test.strip())
