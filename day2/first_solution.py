import re

red_max = 12
green_max = 13
blue_max = 14
total_sum = 0

with open('C:\\Users\\thain\\OneDrive\\ti\\advent_code2023\\day2\\input.txt', 'r') as input:
    for line in input:
        # gets the game ID
        id = re.match("Game ([0-9]*):", line).group(1)

        # parses the draws in each game
        draws = re.match("Game [0-9]*: (.*)", line).group(1).split(";")

        # variable to check if the game is valid - True if valid
        ok = True

        # checks for each color and gets its amount
        for i in draws:
            blue = 0
            green = 0
            red = 0
            if "blue" in i:
                blue = re.search("([0-9]*) blue", i).group(1)
            if "green" in i:
                green = re.search("([0-9]*) green", i).group(1)
            if "red" in i:
                red = re.search("([0-9]*) red", i).group(1)
            if int(blue) > blue_max or int(green) > green_max or int(red) > red_max:
               ok = False

        # adds the game ID to the total_sum if the game is valid
        if ok == True:
            total_sum = total_sum + int(id)

    print(total_sum)


