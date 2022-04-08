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


# /!\ needs review /!\
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

    def fibo(N):
        list = []
        for i in range(1, N)

            list.append()



# 6) Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2.
def question6(N):
    pass


# 7) Given an array of integers, find the sum of its elements.
def question7(N):
    pass


# 8) Given an array, find the largest element in it.
def question8(N):
    pass


def question9(N):
    pass


def question10(N):
    pass


def question11(N):
    pass


def question12(N):
    pass


def question13(N):
    pass


def question14(N):
    pass


def question15(N):
    pass


def question16(N):
    pass


def question17(N):
    pass


def question18(N):
    pass


def question19(N):
    pass


def question20(N):
    pass


def main():
    # question 1:
    # print("Question 1:")
    # num1 = int(input("num1 here: "))
    # num2 = int(input("num1 here: "))
    # print(question1(num1, num2))
    
    # question 2:
    # print("Question 2:")
    # a = int(input("enter 'a' here: "))
    # b = int(input("enter 'b' here: "))
    # print(question2(a, b))

    # question 3:
    # print("Question 3:")
    # start = int(input("Start of range: "))
    # end = int(input("End of range: "))
    # print(question3(start, end))

    # question 4:
    # print("Question 4:")
    # N = int(input("enter 'N' here: "))
    # question4(N)



if __name__ == '__main__':
    main()