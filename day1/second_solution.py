numbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "zero":"0", "0":"0", "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9", "0":"0"}
sum = 0

def first_number(word):
    index_min = len(word)
    number_min = None
    for i in numbers.keys():
        if i in word:
            index = word.find(i)
            if index != -1 and index < index_min:
                index_min = index
                number_min = i
    return number_min 
    

def last_number(word):
    index_max = -1
    number_max = None
    for i in numbers.keys():
        if i in word:
            index = word.rfind(i)
            if index != -1 and index > index_max:
                index_max = index
                number_max = i
    return number_max

  
with open('C:\\Users\\thain\\OneDrive\\ti\\advent_code2023\\day1\\input.txt', 'r') as inputs:
    for line in inputs:
        first = numbers[first_number(line)]
        last = numbers[last_number(line)]
        line_num = []
        line_num.append(first)
        line_num.append(last)
        result = "".join(line_num)
        sum = sum + int(result)
    print(sum)