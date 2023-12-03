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

        # variables to check the min amount of cubes
        blue_min = 0
        red_min = 0
        green_min = 0

        # parses for each color and gets its amount, also checks the min amount of cubes required in each line
        for i in draws:
            blue = 0
            green = 0
            red = 0
            if "blue" in i:
                blue = int(re.search("([0-9]*) blue", i).group(1))
                if blue > blue_min:
                    blue_min = blue
            if "green" in i:
                green = int(re.search("([0-9]*) green", i).group(1))
                if green > green_min:
                    green_min = green
            if "red" in i:
                red = int(re.search("([0-9]*) red", i).group(1))
                if red > red_min:
                    red_min = red

        # calculates de power of the line and total sum
        power = blue_min * green_min * red_min
        total_sum = total_sum + power

print(total_sum)


 


