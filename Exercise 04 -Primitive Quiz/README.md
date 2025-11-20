## Exercise 4: Primitive Quiz - 30 Marks

In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.
```python

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


