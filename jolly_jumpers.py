import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.rstrip()
        sequence = [int(s) for s in test.split() if s.isdigit()]
        differnce = [abs(sequence[i+1]-sequence[i]) for i in range(len(sequence)-1) ]
        output = 'Jolly'

        if len(differnce) > 0:
            diff_set = range(1,(max(differnce)+1))
            for i in diff_set:
                if i not in differnce:
                    output = 'Not jolly'
        print output
