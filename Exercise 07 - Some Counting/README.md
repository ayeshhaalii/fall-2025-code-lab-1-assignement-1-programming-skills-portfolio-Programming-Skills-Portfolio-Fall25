## Exercise 7: Some Counting - 20 Marks

Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
in each case.
* Write a loop that counts up from 0 to 50 in increments of 1.
* Write a loop that counts down from 50 to 0 in decrements of 1.
* Write a loop that counts up from 30 to 50 in increments of 1.
* Write a loop that counts down from 50 to 10 in decrements of 2.
* Write a loop that counts up from 100 to 200 in increments of 5.
*You may include all loops in a single project*

# Loop 1: Count up from 0 to 50 in increments of 1
print("Loop1:")
for i in range (0, 51, 1): 
    print(i)
 
# Loop 2:Count down from 50 to 0 in decrements of 1
print("\nLoop2:")
for i in range (50, -1, -1): 
    print(i)

# Loop3: Count up from 30 to 50 in increments of 1 
print("\nLoop3:")
for i in range (30, 51, -1): 
    print(i)

# Loop4: Count down from 50 to 10 in decrements of 2
print("\nLoop4:")
for i in range (50, 9 , -2): 
    print(i)

# Loop5: Count up from 100 to 200 in increments of 5
print("\nLoop5:")
for i in range (100, 201 , 5): #Starts from 100, ends at 200, increases by 5
    print(i)
