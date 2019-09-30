# ### Problem 1
# Ask the user to enter a number. 
# Using the provided list of numbers, use a for loop to iterate the array and print out all the values that are smaller than the user input and print out all the values that are larger than the number entered by the user.

# ```
# Start with this List
list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]
# ```
# Example Input/Output if the user enters the number 9:
# ```
# The User entered 9
# 1  2  7 are smaller than 9
# 12  24  34  10 are larger than 9
# ```

# create variable to take userinput
usernum = int(input("Enter a number: "))
# iterate through list of numbers. create conditional to read if user number is bigger or smaller than the other
for each in list_of_many_numbers:
    if usernum > each:
        print(f" {each} is smaller than {usernum}")
    elif usernum < each:
        print(f" {each} is greater than {usernum}")
