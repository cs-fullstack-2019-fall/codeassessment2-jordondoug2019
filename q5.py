# ### Problem 5
# Create a SportsTeam Class for tracking sports teams. The class should have the properties team_name_p, team_city, and team_ranking_p.
# The class should have a method to change a Team’s ranking. 
# The class should implement the ```__str__``` method so that when an instance of the SportsTeam is printed it will output a string containing the team name, team city, and team rank (use f strings to format the output).
# Your program should create a SportsTeam instance with an initial ranking of 2.
# Print out the class.
# Your program should change the ranking of the team to 8 using only the class method.
# Print out the class (should use your ```__str__``` method).


# Example Output:
# ```
# The Grizzlies are from Memphis and are 2 in the standings.
# # Update the rating from 2 to 8 from your code
# The Grizzlies are from Memphis and are 8 in the standings.
# ```

# create class for Sportsteam that has 2 properties
# cretae method that has changes ranking prop.
# created print method that prints class
class SportsTeam:
    def __init__(self, name, city, ranking):
        self.name = name
        self.city = city
        self.ranking = ranking
    def changerank(self):
        newranking = int(input("Enter a new ranking: "))
        self.ranking = newranking
        return f"The new ranking for {self.name} is {self.ranking}"
    def __str__(self):
        return f" {self.name} {self.city} {self.ranking}"

#
newTeam = SportsTeam("seahawks", "seattle", 2)
print(newTeam)
print(newTeam.changerank())