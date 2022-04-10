# general purpose functions to reuse

# splits a string to a list by delimiter " "
def split_list_from_string(string):
    string_list = string.split(" ")
    return string_list

# convert a list of string numbers to integers
def list_string_2_int(list):
    new_list = []
    for i in range(0, len(list)):
        new_list.append(int(list[i]))
    return new_list

# filters out misc symbols from string - general purpose
def remove_symbols(string):
    clean_string = string
    unwanted_chars = "!@#$%^&*()_+{}\|:'<>/[,]"
    for char in unwanted_chars:
        clean_string = clean_string.replace(char, "")
    # expected output 9 8 10 122 1290
    return clean_string


def main():
    # for debugging
    list_input = ['1', '2', '3']
    x = list_string_2_int(list_input)

    list_string = str(list_input)
    print(remove_symbols(list_string))


if __name__ == '__main__':
    main()