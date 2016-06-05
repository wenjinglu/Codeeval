import sys
import re

candy_value = {'Vampires': 3, 'Zombies': 4, 'Witches': 5}

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test_value = test.split(', ')
        input_dict = {}
        for item in test_value:
            item_split = item.split(': ')
            input_dict[item_split[0]] = int(item_split[1])
        candies = 0
        n_cos = 0
        for cos in candy_value:
            candies = candies + candy_value[cos]*input_dict[cos]
            n_cos = input_dict[cos]+n_cos
        candies = candies * input_dict['Houses']
        print candies/n_cos
