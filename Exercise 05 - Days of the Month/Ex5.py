# Create a dictionary 
days_in_month={
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31, 
    6: 30, 
    7: 31,
    8: 31,
    9: 30,
    10: 31, 
    11: 30,
    12: 31
}
month = int(input("Enter the month number(1-12):")) #ask user for input 
if 1 <= month <= 12: #validate input
    if month == 2:
       leap = input("Is it a leap year? (yes or no)")
       if leap == "yes":
             print ("February has 29 days.")
       else:
             print("Februaruy has 28 days.")
    else:
         print ("Month{month} has {days_in_month[month]} days.")
else:
     print ("Invalid month number! Please enter a number between 1 and 12.")