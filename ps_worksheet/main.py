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
#

long_string = 'aaabbbbbcccccdddeeeeeeefffgggggggggggggghhhhhhhhiiiiiiiijjjjjj'