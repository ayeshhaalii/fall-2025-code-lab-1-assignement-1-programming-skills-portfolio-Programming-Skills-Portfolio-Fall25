# List of names 
names = ("Jake", "Zac", "Ian", "Ron", "Sam", "Dave")

# Ask user for input
search_term = input("Enter the name you want to search for:")

# Check if the name is in the list 
if search_term in names:
   print(f"{search_term} is found in the list!")
else: 
    print(f"{search_term} is not found in the list!")