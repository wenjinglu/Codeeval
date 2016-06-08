import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        num_list = test.split()
        num_list = [int(j) for j in num_list]
        result = []
        for i in range(1,num_list[2]+1):
            if i % num_list[0] == 0 and i % num_list[1] == 0:
                result.append('FB')
            elif i % num_list[0] == 0:
                result.append('F')
            elif i % num_list[1] ==0:
                result.append('B')
            else:
                result.append(str(i))

        print ' '.join(result)
#        print '\n'
