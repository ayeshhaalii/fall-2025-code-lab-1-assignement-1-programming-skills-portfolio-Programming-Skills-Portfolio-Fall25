#Create an empty dictionary
person = {}

#Get user input
person["name"] = input ("Enter your full name:")
person ["hometown"] = input ("Enter your hometown:")

#Trying to ensure age is entered as number
while True: 
    try: 
        person["age"] = int(input("Enter your age:"))
        break
    except ValueError:
        print("Please enter your age as a number (e.g.,20).")

#Print the information
print(f"\nName: {person['name']}\nHometown: {person['hometown']}\nAge: {person['age']}")
