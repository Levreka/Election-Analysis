print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
# This code was comment out because variable holding the list 
# was created on line 2 of the code
# code will run normal it doesn't required the code on line 9
# it does run normal even with that code not comment out
# counties = ["Arapahoe","Denver","Jefferson"]

# line of code shows how to use membership operators in and not in
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


# this line of code is combining membership operators 
# and logical operators into one code 20-23 lines 
# are using "and" logical operators "in" membership operators 
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# line 27-30 are using logical operator "or" membership operator "in"
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

# line 33-37 are using logical operator "or" 
# membership operator "in" also "not in"
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# practicing for loop also know as count-controlled loop
# it will continue to loop throught the counties 
# until it has no more items to loop over
for county in counties:
    print(county)
# creating a new variable that holds a list
numbers = [0, 1, 2, 3, 4]
# starting the for loop to print all numbers in our list
for num in numbers:
    print(num)
# for loop using range function to print all the numbers in list
for num in range(5):
    print(num)
# The variable i is used to indicate the index, or the values 0, 1, and 2, in the length of the counties list. The letter i is often used for simplicity, but any variable can be used.
# Inside the range() function, we get the length of the list of counties, which is the integer 3.
# Then, we iterate through the list, where the variable i is equal to 0 for the first index. The 0 is passed into the print(counties[i]) statement, where i = 0, and "Arapahoe" is printed.
# This process is continued until all three items, or counties, in the list are printed to the screen.
for i in range(len(counties)):
    print(counties[i])

counties_tuples = ("Arapahoe","Denver","Jefferson") 
for i in range(len(counties_tuples)):
    print(counties_tuples)
for county in counties_tuples:

      print(county)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
for county, voters in counties_dict.items():
    print(county, voters)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
for i in range(len(voting_data)):

      print(voting_data[i])

for i in range(len(voting_data)):

      print(voting_data[i])
for county in range(len(voting_data)):

     print(county)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
for county_dict in voting_data:

     print(county_dict['registered_voters'])
for county_dict in voting_data:
    print(county_dict['county'])
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
for county, voters in counties_dict.items():
    print(f"{ county } county has { voters } registered voters.")
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)
