import random
# problem solving worksheet

# 1. Reverse a string 
# To reverse a string I would start out by finding the length of the string. If I knew what the string was, 
# I could simply do a for loop and input the index numbers starting with the higher index number to the lower and have 
# # it print in the indexes of the word reverse order. I would then use the second for loop to compress the word onto one line.

# word = 'hello'
# for index in range(4,-1,-1):
#     print(word[index])

# new_word = ' '
# for index in range(4, -1, -1):
#     new_word += word[index] 
# print(new_word)

# # # If I didn't know the length of the word, or I would want to account for user input, I would input len(word) - 1 in place of 
# # # the higher index number. This accounts for the possible changing length of the word, but still completing the same task. 

# task = 'knitting'
# for index in range(len(task)-1,-1,-1):
#     print(task[index])

# new_task = ' '
# for index in range(len(task) -1, -1, -1):
#     new_task += task[index] 
# print(new_task)


# # # or

# sport = 'quidditch'
# for index in range(len(sport)-1,-1,-1):
#     print(sport[index])

# new_sport = ' '
# for index in range(len(sport) -1, -1, -1):
#     new_sport += sport[index] 
# print(new_sport)

# # 2. Capitalize a letter

# # To capitalize a letter is involves a for loop, but we are making a condition for the first index of each word. To do this I 
# # would start with the regular for loop:

# phrase = 'hello world'
# for index in range(0,len(phrase)):
#     print(phrase[index])

# This keeps the space in between the words and prints them as written. Next I would add use the second for loop to bring them
# onto one line, and the .title() to capitalize the first letter of each word, as if it were a title. 

# phrase = 'hello world'
# for index in range(0,len(phrase)):
#     print(phrase[index]) 
# new_phrase = ' '
# for index in range(0,len(phrase)):
#     new_phrase += phrase[index] 
# print(new_phrase.title())

# 3. Compress a string of characters
# In order to compress a string there are several steps that must be done. Essentially you will need to iterate over each letter
# 

# def compress(string):
#     index = 0
#     compressed = ""
#     len_str = len(string)
#     while index != len_str:
#         count = 1
#         while (index < len_str-1) and (string[index]) == string[index+1]:
#             count = count + 1
#             index = index + 1
#         if count == 1:
#             compressed += str(string[index])
#         else:
#             compressed += str(string[index]) + str(count)
#         index = index + 1
#     return compressed

# string = 'aaabbbbbcccccdddeeeeeeefffgggggggggggggghhhhhhhhiiiiiiiijjjjjj'
# print(compress(string))

# 4. Bonus challenge - Palindrome
    # function argument is start at the end, count down to the beginning, stepping backwards one at a time" 
    #example: slice notation has three parts, start, stop, step. [::3] beginning to end, counting by 3, [::-3] end to
    #beginning counting down by three. 

    # To check if a user input is a palindrome, create a function that compares the user input with its own reverse.
    # if they match, then the input is a palindrome. If they don't, then it is not a palindrome. 

# def palindrome_checker(str):
#     return str == user_input[::-1]

# user_input = input('Please enter your palindrome: ')

# str = user_input
# output = palindrome_checker(str)

# if output:
#     print("This is a palindrome.")
# else:
#     print("This is not a palindrome.")

# worksheet two

# 1. Happy Numbers
# A happy number starts with a positive integer, replacing the sums of the squares of its digits, and repeating
# repeating the process until the number equals 1. Ex. 10. 1^2 + 0^2 = 1 If a number is not happy, it is sad.
# Start with an integer. If number is greater than 0, calculate remainder by dividing by 10. Calculate square of 
# remainder and add it to a variable sum. Divide by 10. Keep repeating until the sum of the square of all digits 
# have been calculated. Return sum. Then determine if the result meets the qualifications of a happy number, and 
# print if yes, otherwise it is a sad number.

# def is_happy(num):
#     rem = sum = 0;

#     while (num>0):
#         rem = num%10;
#         sum = sum + (rem*rem);
#         num = num//10;
#     return sum;

# num = int(input("Please enter number to check: "))
# result=num;

# while(result !=1 and result !=4):
#     result = is_happy(result)

# if(result == 1):
#     print(str(num) + " is a happy number");
# else:
#     print(str(num)+ " is a sad number");

# 2. Prime numbers
# Prime number is a number that is only divisible by one and itself. Ex. 7, 3, 5. 
# A method to print out all prime numbers between 0 and 100 would be to define the 
# variables between the first integer and the second integer in the desired range.
# Then you need to add the condition that the number needs to be greater than one, 
# and if it is not divisible by a number in a range. 



# for x in range(1,100):
#     if x / x == 1 and x / 1 == x:
#         for number in range(1,100):
#             x != number

# for x in range(2,100):
#     i = list[range(2,100)]
#     if x % i == 0:
#         print(x)

# def is_prime(x):
#     if x > 1:
#        return False
#     for i in range(2,100):
#         if x % i == 0:
#             return False
#     return True

# def prime_range(num):
#     num = random.randint <= 2 >= 100

# is_prime(prime_range)

# this one works

# first_int = 2
# second_int = 100

# print("Prime numbers between", first_int, "and" , second_int, "are: ")

# for num in range (first_int, second_int):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

# Fibonacci 

def fibonacci_of(n):
    if n in {0,1}:
        return n
    return fibonacci_of(n-1) + fibonacci_of(n-2)

[fibonacci_of(n) for n in range(1,100)]