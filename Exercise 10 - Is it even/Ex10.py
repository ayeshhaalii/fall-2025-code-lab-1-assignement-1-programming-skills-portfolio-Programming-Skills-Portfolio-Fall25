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
