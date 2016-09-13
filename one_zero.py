import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test_list = test.split()
        n0 = int(test_list[0])
        num = int(test_list[1])

        result = 0
        for i in range(1,num+1):
            temp = str(bin(i)[2:])
            temp_n0 = sum([int(x) == 0 for x in temp])
            if temp_n0 == n0:
                result = result + 1

        print result
