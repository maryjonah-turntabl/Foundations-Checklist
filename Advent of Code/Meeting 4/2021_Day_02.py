# function to read data and split to list of list of strings
def clean_data():
    with open('./2021_day_02_data.txt', 'r') as fileObj:
        list_directions = [line.split() for line in fileObj]
        return list_directions


# save input data to a variable
cleaned_data = clean_data()

# returns the position of the submarine


def submarine_position(list_str_direction):
    width = depth = 0

    movement = list_str_direction[0]
    value = int(list_str_direction[1])

    if movement == "forward":
        width += value
    elif movement == "down":
        depth += value
    elif movement == "up":
        depth -= value

    return depth, width


# function to "reduce" a collection of elements into a single value
def productDepthWidth(function, collection):
    widthResult = depthResult = 0

    for item in collection:
        valOne, valTwo = function(item)
        widthResult += valOne
        depthResult += valTwo

    return widthResult * depthResult


answer = productDepthWidth(submarine_position, cleaned_data)
print(answer)
