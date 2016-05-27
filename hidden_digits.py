import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        #test = test.rstrip()
        letter = 'abcdefghij'
        number = '0123456789'
        output = ''
        for i in test:
            if i in number:
                output = output+i
            if i in letter:
                output = output + number[letter.index(i)]
        if output:
            print output
        else:
            print None
