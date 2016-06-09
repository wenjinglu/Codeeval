import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test_list = test.split()
        num_list = [i for i in test_list[0].strip()]
        pattern = test_list[1].strip()
        if '+' in  pattern:
            pattern_list = pattern.split('+')
            len1 = len(pattern_list[0])
            list1 = num_list[:len1]
            list2 = num_list[len1:]
            num1 = int(''.join(list1))
            num2 = int(''.join(list2))
            print num1 + num2
        else:
            pattern_list = pattern.split('-')
            len1 = len(pattern_list[0])
            list1 = num_list[:len1]
            list2 = num_list[len1:]
            num1 = int(''.join(list1))
            num2 = int(''.join(list2))
            print num1 - num2
