import sys

with open(sys.argv[1], 'r') as test_cases:
    for t in test_cases:
        test = t.split('|')
        name =test[0]
        keys = test[1].split()
        keys = [int(i) for i in keys]
        writer = []
        for key in keys:
            writer.append(name[key-1])
        print ''.join(writer)
