from functools import reduce

# Part 1 - Solution A
with open("input.txt", "r") as file_handler:
    values = file_handler.read().splitlines()

    total_fuel = 0
    for line in values:
        module_fuel = (int(line) // 3) - 2
        total_fuel += module_fuel


# Part 1 - Solution B
with open("./input.txt", "r") as file_obj:
    lines = file_obj.read().splitlines()

    total_fuel_2 = reduce(lambda accumulator,
                          current: accumulator + (int(current) // 3 - 2), lines, 0)
    print("Part 1A:", total_fuel_2)

#################           #################           #################           #################           #################

# Part 2
with open("./input.txt", "r") as file_obj:
    lines = file_obj.read().splitlines()

    def get_fuel(mass):
        fuel = int(mass) // 3 - 2
        return fuel + get_fuel(fuel) if fuel > 0 else 0

    total_fuel_3 = reduce(
        lambda accumulator, current_value: accumulator + get_fuel(current_value), lines, 0)

    print("Part 1B:", total_fuel_3)

