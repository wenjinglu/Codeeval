import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:

        out_seq=[]
        while (test):
            digits = [ int(char) for char in test.strip() ]
            result = sum( i*i for i in digits)
            if result == 1:
                print 1
                break
            else:
                if result in out_seq:
                    print 0
                    break
                else:
                    out_seq.append(result)
                    test = str(result)
