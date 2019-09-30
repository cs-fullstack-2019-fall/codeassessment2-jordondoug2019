# ### Problem 3
# Given 2 lists of claim numbers, write the code to merge the 2 lists provided to produce a new list by alternating values between the 2 lists. Once the merge has been completed, print the new list of claim numbers (DO NOT just print the array variable!)
# ```
# # Start with these lists
list_of_claim_nums_1 = [2, 4, 6, 8, 10]
list_of_claim_nums_2 = [1, 3, 5, 7, 9]
# ```
# Example Output:list_of_claim_nums_2[each]
# ```
# The newly created list contains:     2  1  4  3  6  5  8  7  10  9
# ```
#  Create empty variable array
newclaimList = []

# for each in range(len(list_of_claim_nums_1)):
#     # newclaimList = str(list_of_claim_nums_1[each]) + str(list_of_claim_nums_2[each)
    # print(newclaimList)
# append claim list to new list and print
newclaimList.append(list_of_claim_nums_1)
newclaimList.append(list_of_claim_nums_2)
print(newclaimList)
# created for loop to print each index in list
for each in newclaimList:
    print(newclaimList[::1])
    # newclaimList.append(list_of_claim_nums_2)
    # print(newclaimList[each])
