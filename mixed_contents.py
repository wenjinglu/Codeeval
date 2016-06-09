import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        test_list = test.split(',')
        word = []
        num = []
        for item in test_list:
            try:
                num.append(int(item))
            except:
                word.append(item)
        num = [str(i) for i in num]
        words = ','.join(word)
        nums = ','.join(num)
        if len(nums) == 0:
            print words
        elif len(words) == 0:
            print nums
        else:
            print words + '|'+ nums
