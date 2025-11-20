## Exercise 10: Is it even? - 35 Marks

Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function.

# Function to determine if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
       return "The number is even."
    else:
       return "The number is odd."

# Main function
def main():
 # Ask user for a number
 num = int(input("Enter a number:"))

 # Call the function, store and print the returned message 
 result = check_even_odd(num)
 print(result)

# Run the program
if __name__ == "__main__":
   main()

