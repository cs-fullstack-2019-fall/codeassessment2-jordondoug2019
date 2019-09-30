# ### Problem 4
# Write a program that allows users to compare words by their length. Implement a function called chk_strings that accepts 2 strings entered by the user and compares them by length
# The function should return true if the first string parameter has more characters (i.e. longer) than the second string passed into the function, otherwise, the function should return false.
# DO NOT print the result in the function, print the result using the return value provided by the function. 

# Example Input/Output:
# ```
# Enter the first string: BIRD
# Enter the second string: COW

# BIRD is longer than COW
# ```

# def chk_strings(word1, word2):
#     if word1 == word2[::1]:
#         print(f" {word1} is longer than {word2}")
#         return True
#     else:
#         return False
#
#
# print(chk_strings("Bird", "cow"))

# create function and variables that take user input and compare word length
userinput = input("Enter 1st word: ")
userinput2 =input("enter 2nd word: ")
def chk_strings(word1,word2):
    if word1 > word2[::1]:
        print(f"{word1} is bigger than {word2}")
        return True
    else:
        return False

print(chk_strings(userinput,userinput2))