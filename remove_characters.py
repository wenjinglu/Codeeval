import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        script = test.split(',')
        character = [i for i in script[1].strip()]
        output = []
        for item in script[0]:
            if item not in character:
                output.append(item)
        print ''.join(output)
