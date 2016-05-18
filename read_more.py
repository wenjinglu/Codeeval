import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        if len(test) <= 55:
            print test
        else:
            #whitespace_location = test[:40].rfind(" ")
            #print test[:whitespace_location] + "... <Read More>"
            result = test[:40].rsplit(' ', 1)[0]
            print result + "... <Read More>"
