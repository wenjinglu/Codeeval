import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.rstrip()
        test = [i.lower() if i.isalpha() else ' ' for i in test]
        sentence = ''.join(test)
        test_list = sentence.split()
        print ' '.join(test_list)
