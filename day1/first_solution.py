sum = 0

with open('C:\\Users\\thain\\OneDrive\\ti\\advent_code2023\\day1\\input.txt', 'r') as inputs:
    for input in inputs:
        line_num = []
        line_result = []
        for i in input:
            if i.isdigit():
                line_num.append(i)
        if len(line_num) == 1:
            line_result.append(line_num[0])
            line_result.append(line_num[0])
            result = "".join(line_result)
        else: 
            line_result.append(line_num[0])
            line_result.append(line_num[-1])
            result = "".join(line_result)
        sum = sum + int(result)
    print(sum)