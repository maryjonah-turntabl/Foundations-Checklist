# Part 1B

with open("./input.txt", "r") as file_object:
    stringInput = file_object.read().split(',')
    inputs = list(map(lambda str: int(str), stringInput))
    
def process_intcode(program, index=0):
    opcode = program[index]

    if opcode == 99:
        return program[0]

    numVal1 = program[index + 1]
    numVal2 = program[index + 2]
    answerIndex = program[index + 3]

    if opcode == 1:
        program[answerIndex] = program[numVal1] + program[numVal2]
        index += 4
        return process_intcode(program, index)
    elif opcode == 2:
        program[answerIndex] = program[numVal1] * program[numVal2]
        index += 4
        return process_intcode(program, index)

inputs[1] = 12
inputs[2] = 2
print(process_intcode(inputs))        


# Part 2B
