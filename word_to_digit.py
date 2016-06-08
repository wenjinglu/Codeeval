import sys
num_dict = {"one":1, "two":2, "three":3, "four":4, "five":5,
                "six":6, "seven":7, "eight":8, "nine":9,"zero":0}

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test=test.strip()
        test = test.split(';')
        result = []
        for item in test:
            result.append(num_dict[item])
        result = [str(i) for i in result]
        print ''.join(result)
