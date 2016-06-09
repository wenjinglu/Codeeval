import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        test_list = test.split()
        word = test_list[0]
        word_list = []
        num = test_list[1]
        for i in range(len(word)):
            if num[i] == '1':
                word_list.append(word[i].upper())
            else:
                word_list.append(word[i])
        print ''.join(word_list)
