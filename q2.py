# ### Problem 2
# Prompt the user with the message, ‘Is it better to be rude or kind to People?’ 
# Keeping prompting the user to enter an answer until they enter the word kind. 
# Each time they enter something other than kind, print the message, ‘That’s not the answer I had hoped to hear. Try again.’ and prompt the user again.
# Once the user enters kind, print, ’Now that’s what I wanted to hear!’ and exit the program.

# create a variable that holds userinput
userinput = input("IS it better to be rude or kind to People? ")

# continue to ask user for input until kind is entered. print message based on userinput
while userinput != "kind":
    if userinput != "kind":
        print("That's not the answer I had hoped to hear. Try again.")
        userinput = input("Is it better to be rude of kind to people? ")
    if userinput == "kind":
            print("Now that's what I wanted to hear")