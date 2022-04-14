# Day 1A
# read input and convert to list of numbers
with open("./input.txt", "r") as file_obj:
    strInput = file_obj.read().split()
    intInput = list(map(lambda str: int(str), strInput))

# takes list of numbers and result, returrns product and 2 numbers that add up to result
def find_product_two(listNum, result):
    for intNum in listNum:
        difference = result - intNum
        if difference in listNum:
            return intNum * difference, intNum, difference                 

print(find_product_two(intInput, 2020))


#########################################################################################################################


# Day 1B
def find_product_three(listNum, result):
    for intNum in listNum:
        for secIntNum in listNum:
            difference = result - intNum - secIntNum
            if difference in listNum:
                return difference * intNum * secIntNum, difference, intNum, secIntNum

print(find_product_three(intInput, 2020))                