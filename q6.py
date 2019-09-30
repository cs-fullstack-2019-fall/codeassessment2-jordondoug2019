# ### Problem 6
# Create a class called ClubMember 
# Each club member has a name and a role  
# Create ClubMember instances for the following people:
# ```
# Alfred - Club President
# Troy - Club Vice President
# Albert - Club Secretary
# Bob - Club Treasurer
# ```
# Add each member instance to a new club_members list that you create.
# Write the code needed to loop through the club member list and print the current number of members in the list, then the member’s name and club role, one per line using f strings.

# Example Output:
# ```
# There are currently 4 club members in the list!

# Club President: Alfred
# Club Vice President: Troy
# Club Secretary: Albert
# Club Treasurer: Bob
# ```

# create class for clubmember with print method
class Clubmember:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def __str__(self):
        return f"{self.name} {self.role} \n"

# create multiple instances of Clubmember
mem1 = Clubmember("Alfred", "Club President")
mem2 = Clubmember(" Troy", "Club Vice President")
mem3 = Clubmember("Albert", "Club Secretary")
mem4 = Clubmember("Bob", "Club Treasurer")

# create list of club members
newclubmembers = [mem1, mem2, mem3, mem4]

# create for loop that iterates through each index and prints name of members
for each in range(len(newclubmembers)):
    print(newclubmembers[each])
    # print(f"{newclubmembers[0]}"
    #       f"{newclubmembers[1]}"
    #       f"{newclubmembers[2]}"
    #       f"{newclubmembers[3]}")
