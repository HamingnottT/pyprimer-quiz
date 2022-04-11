import utils as u
import re

# 1) Given two numbers num1 and num2. The task is to write a Python program to find the addition of these two numbers.
def question1(num1, num2):
    return num1 + num2


# 2) Given two numbers, write a Python code to find the Maximum of these two numbers.
def question2(a, b):
    # adds a and b to list
    list = []
    list.append(a)
    list.append(b)

    # Approach 1 - saving this for educational purposes
    # counter = 0
    # for num in list:
    #     try:
    #         if num > list[num + 1]:
    #             counter += 1
    #             break
    #     except IndexError:
    #         break

    # return list[counter]

    # Approach 2 - more efficient
    max = list[0]
    for num in list:
        if num > max:
            max = num

    return max


# /!\ needs attention /!\
# 3) Given two positive integers start and end. The task is to write a Python program to print all Prime numbers in an Interval.
def question3(start, end):

    interval = []
    for num in range(start, end):
        interval.append(num)


    prime_list = []
    composite_list = []

    for i in interval:
        if (i % 2 == 0):
            composite_list.append(i)
        elif (i % 2 > 0):
            prime_list.append(i)

    return f"{prime_list}"


# 4) Given a positive integer N, The task is to write a Python program to check if the number is prime or not.
def question4(N):
    
    # A prime number cannot be divided completely
    
    # Approach 1: brute force
        # starts loop by first halving the number and then continuing thru the loop
        # each input should break at 2, but a range of 2 to 100 is added just incase
    # for i in range(2, 100):
    #     if (N % i == 0) and (i != N):
    #         print("This number is probably composite")
    #         break
    #     elif (N % i > 0) and (i != N):
    #         print("This number is probably prime")
    #         break

    # Approach 2: modding only by 2
    if N % 2 == 0:
        print("This number is probably composite")
    else:
        print("This number is probably prime")


# 5) Given a number \’n\’, how to check if n is a Fibonacci number. First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, .. 
def question5(N):
    list = []
    N = N
    range_int = 100     #fixed to 100

    # constructed fibonacci sequence to analyze logic and use as basis for answer
    def fibo(range_int):
        # global list     #global list so that I can access this fibo list in other functions
        

        for i in range(0, range_int):
            if i == 0:
                list.append(0)
            elif i == 1:
                list.append(1)
            else:
                list.append(list[i-1]+list[i-2])

    fibo(range_int)

    def check_fibo(N):
        pos_match = 0
        for i in list:
            if N == i:
                pos_match += 1
            else:
                pass

        if pos_match >= 1:
            print("Yes, this is a fibonacci number.")
        else:
            print("No, this is not a fibonacci number.")

    check_fibo(N)


# 6) Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2.
def question6(N):
    list = []
    list_sq = []
    
    for i in range(1, N + 1):
        list.append(i)
    
    for i in list:
        list_sq.append(i ** 2)

    result = sum(list_sq)

    print(result)


# 7) Given an array of integers, find the sum of its elements.
def question7(N):
    array = N.split(" ")                # create list from string
    for i in range(0, len(array)):      # iterate thru array's length
        array[i] = int(array[i])        # convert string values to integer

    # method 1:                         # use the sum function on the list - the cheap way!
    # print(sum(array))                 
    
    # method 2:                         # for loop to iterate thru the array list values incrementing to variable sum
    sum = 0
    for i in array:
        sum += i

    print(sum)

# 8) Given an array, find the largest element in it.
def question8(N):
    array = N.split(" ")                # create list from string
    for i in range(0, len(array)):      # iterate thru array's length
        array[i] = int(array[i])        # convert string values to integer

    # attempt 1:                        # Wierd results - keeping for self education
    # max_list = []
    # for i in range(1, len(array)):
    #     if array[i] > array[i - 1]:
    #         max_list.append(array[i])
    
    # print(max_list)

    # for i in range(1, len(max_list)):
    #     if max_list[i] > max_list[i - 1]:
    #         max_list.append(array[i])
        
    # print(max_list)

    # attempt 2:                        # sort array and then return the maximum number at the beginning
    arr_sorted = sorted(array, reverse=True)
    result = int(arr_sorted[0])
    print(arr_sorted[0])


# 9) Given multiple numbers and a number n, the task is to print the remainder after multiply all the number divide by n.
def question9(list, N):
    array = list.split(" ")
    array_product = 1                   # not 0 because the first index product would be zero

    for i in range(0, len(array)):      # iterate thru array's length
        array[i] = int(array[i])        # convert string values to integer

    for i in array:
        array_product = array_product * i

    result = array_product % N          # mod by N for remainder

    print(result)


# 10) Split the array [12, 30, 25, 16, 23, 14],  and move the first part of array add to the end.
def question10(list, k):
    list = u.split_list_from_string(list)       
    list = u.list_string_2_int(list)            # set problem up by converting list of string to list of integers using utils custom module
    
    # attempt 1: 
    first_int = list[:k]                         # store first integers in its own variable
    split_list = list[k:]                               

    result = split_list + first_int

    print(result)

# 11) Given a list, write a Python program to swap first and last element of the list.
def question11(list):
    list = u.split_list_from_string(list)       # splits string of numbers into list of string numbers
    list = u.list_string_2_int(list)            # converts string list to integer list

    # attempt 1:
    print(f"Before: {list}")
    first_int = list[0]                         # retains the value of the first integer
    last_int = list[-1]                         # retains the value of the last integer

    list.remove(list[0])                        #removes the first integer of the list
    list.remove(list[-1])                       #removes the last integer of the list

    list.append(first_int)                      #appends the first int to the last position
    list.insert(0, last_int)                    #inserts the last int to the head of the list

    print(f"After: {list}")


# 12) Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
def question12(list, pos1, pos2):
    list = u.split_list_from_string(list)
    list = u.list_string_2_int(list)
    pos1 = pos1
    pos2 = pos2

    int1 = list[(pos1 - 1)]
    int2 = list[(pos2 - 1)]

    list.remove(int1)
    list.remove(int2)

    list.insert((pos1 - 1), int2)               # wrote pos1 - 1 to ensure value is inserted in the currect location
    list.insert((pos2 - 1), int1)

    print(list)


# 13) Write a program to reverse a list in a python.
def question13(list):
    list = u.split_list_from_string(list)
    list = u.list_string_2_int(list)

    print(list)
    list.reverse()                            #or sorted(list, reverse=True)
    print(list)


# 14) Given a list of numbers, the task is to write a Python program to find the smallest number in given list.
def question14(list):
    list = u.split_list_from_string(list)
    list = u.list_string_2_int(list)

    sorted_list = sorted(list)
    result = sorted_list[0]
    print(result)


# 15) Write a program to remove an empty list from list
def question15(list):
    int_list = []

    for i in list:
        if type(i) == int:
            int_list.append(i)

    print(int_list)


# 16) Given a list in Python and a number x, count number of occurrences of x in the given list.
def question16(list, x):
    list = u.split_list_from_string(list)
    list = u.list_string_2_int(list)

    x_counter = 0

    for i in list:
        if i == x:
            x_counter += 1

    print(x_counter)


# /!\ needs attention
# 17) Given two lists, sort the values of one list using the second list
def question17(list1, list2):
    list1 = u.split_list_from_string(list1)
    list2 = u.split_list_from_string(list2)
    list2 = u.list_string_2_int(list2)

    dict = {}

    for i in range(0, len(list2)):
        dict[list2[i]] = list1[i]

    print(dict)


# 20) Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.
def question20(string):

    if string == string[::-1]:
        print("Yes")
    else:
        print("No")


# 21) Given a string. The task is to print all words with even length in the given string.
def question21(string):
    string_list = u.split_list_from_string(string)

    print("\nmethod 1:\n")                      # keeping this version in here because it prints to one line
    for i in string_list:
        if len(i) % 2 != 0:
            string_list.remove(i)

    string_list = str(string_list)
    result = u.remove_symbols(string_list)
    
    print(result)

    string_list = u.split_list_from_string(string)

    print("\nmethod 2:\n")                      # this method is true to the expected output of the question
    for i in string_list:
        if len(i) % 2 != 0:
            string_list.remove(i)

    for i in string_list:
        print(i)  


# /!\ needs attention
# 22) Given a string str. The task is to check whether it is a binary string or not.
def question22(string):
    non_binary_chars = "qwertyuiop[]_+asdfghjkl:'\"/<>,.zxcvbnm23456789!@#$%^&*()=-"

    try:
        binary = [re.findall("01", string)[0], re.findall("10", string)[0], re.findall("11", string)[0], re.findall("00", string)[0]]
    except IndexError:
        # IndexError is thrown on regular strings
        # not known why but this is a short term handling for functionality - resular binary character will show match positive

        pass
    # clean_string = string
    # unwanted_chars = "!@#$%^&*()_+{}\|:'<>/[,]"
    # for char in unwanted_chars:
    #     clean_string = clean_string.replace(char, "")
    # # expected output 9 8 10 122 1290
    # return clean_string

# /!\ needs attention
# 23) Given a dictionary in Python, write a Python program to find the sum of all items in the dictionary.
def question23(key, value):
    key = u.split_list_from_string(key)
    value = u.split_list_from_string(value)
    value = u.list_string_2_int(value)
    dict = {}
    for i in key:
        dict[i]

    print(dict)

# 25) Given an array of words, print all anagrams together
def question25(list):
    list = u.split_list_from_string(list)
            

def main():
    
    print("Please enter question number to get started.")

    option = int(input("> "))

    while option != 0:
        if option == 1:
            # question 1:
            print("Question 1:")
            num1 = int(input("num1 here: "))
            num2 = int(input("num1 here: "))
            print(question1(num1, num2))
            
        elif option == 2:
            # question 2:
            print("Question 2:")
            a = int(input("enter 'a' here: "))
            b = int(input("enter 'b' here: "))
            print(question2(a, b))

        elif option == 3:
            # question 3:
            print("Question 3:")
            start = int(input("Start of range: "))
            end = int(input("End of range: "))
            print(question3(start, end))

        elif option == 4:
            # question 4:
            print("Question 4:")
            N = int(input("enter 'N' here: "))
            question4(N)

        elif option == 5:
            # question 5:
            print("Question 5:")
            N = int(input("enter 'N' here: "))
            question5(N)

        elif option == 6:
            # question 6:
            print("Question 6:")
            N = int(input("enter 'N' here: "))
            question6(N)

        elif option == 7:
            # question 7:
            print("Question 7:")
            array_str = input("Input list of numbers (space in between): ")
            question7(array_str)

        elif option == 8:
            # question 8:
            print("Question 8:")
            array_str = input("Input list of numbers (space in between): ")
            question8(array_str)

        elif option == 9:
            # question 9:
            print("Question 9:")
            list = input("Input list of numbers (space in between): ")
            N = int(input("N = "))
            question9(list, N)

        elif option == 10:
            # question 10:
            print("Question 10:")
            list_input = input("Input list of numbers (space in between): ")
            k_input = int(input("k = "))
            question10(list_input, k_input)

        elif option == 11:
            # question 11:
            print("question 11:")
            list_input = input("Input list of numbers (space in between): ")
            question11(list_input)

        elif option == 12:
            # question 12:
            print("question 12:")
            list_input = input("Input list of numbers (space in between): ")
            pos1 = int(input("Position 1: "))
            pos2 = int(input("Position 2: "))
            question12(list_input, pos1=pos1, pos2=pos2)

        elif option == 13:
            # question 13:
            print("question 13:")
            list_input = input("Input list of numbers (space in between): ")
            question13(list_input)

        elif option == 14:
            # question 14:
            print("question 14:")
            list_input = input("Input list of numbers (space in between): ")
            question14(list_input)

        elif option == 15:
            # question 15:
            print("question 15:")
            list_input = [5, 6, [], 3, [], [], 9]
            question15(list_input)

        elif option == 16:
            # question 16:
            print("question 16:")
            list_input = input("Input list of numbers (space in between): ")
            x = int(input("x = "))
            question16(list_input, x=x)

        elif option == 17:
            # question 17:
            print("question 17:")
            list_input1 = input("Input list of numbers (space in between): ")
            list_input2 = input("Input list of numbers (space in between): ")
            question17(list_input1, list_input2)

        elif option == 18:
            # question 18:
            print("question 18:")

        elif option == 19:
            # question 19:
            print("question 19:")

        elif option == 20:
            # question 20:
            print("question 20:")
            str_input = input("Enter string here: ")
            question20(str_input)

        elif option == 21:
            # question 21:
            print("question 21:")
            str_input = input("Enter string here: ")
            question21(str_input)

        elif option == 22:
            # question 22:
            print("question 22:")
            str_input = input("Enter string here: ")
            question22(str_input)

        elif option == 23:
            # question 23:
            print("question 23:")
            key_input = input("Enter key here: ")
            value_input = input("Enter value here: ")
            question23(key_input, value_input)

        elif option == 24:
            # question 24:
            print("question 24:")

        elif option == 25:
            # question 25:
            print("question 25:")
            list_input = input("Input list of numbers (space in between): ")
            question25(list_input)

        else:
            print("\nInvalid response, please try again.\n")

        print("\n")
        print("Please enter question number to get started.")    
        option = int(input("> "))
    # pass   
    print("\nEnding program. . .\n")

if __name__ == '__main__':
    main()