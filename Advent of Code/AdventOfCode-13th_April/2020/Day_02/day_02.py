# Day 2A
# returns a tuple of the individual needed details
def clean_lines(list_policies):
    char_range, char, password = list_policies.split()

    char_start_range = int(char_range.split("-")[0])
    char_end_range = int(char_range.split("-")[1])
    char = char[0]

    return char_start_range, char_end_range, char, password

# opens file, cleans and returns a list
with open("./input.txt", "r") as file_obj:
    lines = file_obj.read().splitlines();
    data_list = [clean_lines(line) for line in lines]

# returns count of valid password according to policy
def count_valid_password(row_password):
    count_valid_passwords = 0

    for info in row_password:
        min_count, max_count, valid_char, password =  info
        
        if password.count(valid_char) >= min_count and password.count(valid_char) <= max_count:
            count_valid_passwords += 1

    return count_valid_passwords

print(count_valid_password(data_list))


#########################################################################################################################


# Day 2B

def count_valid_password_in_position(row_password):
    count_valid_password_in_position = 0

    for info in row_password:
        min_count, max_count, valid_char, password = info 

        if password[min_count - 1] == valid_char and password[max_count - 1] != valid_char:
            count_valid_password_in_position += 1
        elif password[min_count - 1] != valid_char and password[max_count - 1] == valid_char:
            count_valid_password_in_position += 1

    return count_valid_password_in_position

print(count_valid_password_in_position(data_list))
