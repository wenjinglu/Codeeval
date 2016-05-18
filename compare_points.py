import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        loc = test.split()
        loc1 = float(loc[2]) - float(loc[0])
        loc2 = float(loc[3]) - float(loc[1])

        if loc1 == 0 :
            if loc2 == 0:
                direction = "here"
            elif loc2 > 0:
                direction = "N"
            else:
                direction = "S"
        elif loc1 > 0:
            if loc2 == 0:
                direction = "E"
            elif loc2 > 0:
                direction = "NE"
            else:
                direction = "SE"
        else:
            if loc2 == 0:
                direction = "W"
            elif loc2 > 0:
                direction = "NW"
            else:
                direction = "SW"
        print direction + "\n"
