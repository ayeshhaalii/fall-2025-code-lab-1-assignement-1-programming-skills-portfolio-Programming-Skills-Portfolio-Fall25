#European Capitals Quiz
#Dictionary storing capitals
capitals = {
    "France": "Paris" ,
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Switzerland": "Bern",
    "Austria": "Vienna",
    "Greece": "Athens"
}

print("Welcome to the European Capitals Quiz!")
print("Let's see how many capitals you know.\n")

score = 0 #To keep track of correct answers

#Loop through each country in the dictionary
for country, capital in capitals.items():
    answer = input(f"What is the capital of {country}?").strip().lower()
    if answer == capital.lower():
        print("The answer is correct\n")
        score += 1
    else:
        print(f"Wrong Answer! The correct answer is {capital}.\n")

#Final Score
print(f"Quiz Over! You got {score} out of {len(capitals)} correct.")