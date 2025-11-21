# Define the correct password: 
correct_password = "12345"

# Maximum Attempts
attempts_left = 5
while attempts_left > 0 :
     user_input = input("Enter the password:")
     if user_input == correct_password:
         print("Access granted! Password is correct.")
         break
     else:
          attempts_left -= 1
          print(f"Incorrect Password! Attempts left:({attempts_left})")
          
# If all attempts are used
if attempts_left == 0:
    print ("Maximum attempts reached! Authorities have been alerted.")