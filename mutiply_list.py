import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.split('|')
        list1 = test[0].split()
        list2 = test[1].split()

        result = []
        for i in range(len(list1)):
            result.append(int(list1[i])* int(list2[i]))
        result = [str(i) for i in result]
        print ' '.join(result)
