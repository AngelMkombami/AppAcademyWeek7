   #Loops
    #for loop used to excute a block of code when the condition is true
fruits = ["apple", "banana", "cherry"]
    
for fruit in fruits:
        print (fruit)
    
numbers = [1, 2, 3, 5, 7]
for number in numbers:
      print (number)
      
 #while loop used to excute a certain block of code as long as a certain condition is true
 # using a while loop tto count from 1-5
 # count continues to iterate as long as its less than 5
 
count = 1
while count <= 5:
    print(count)
    count += 1 # increments the count by 1
    
    
#loop control statements

# using break statement
fruits = ["apple", "banana", "cherry" , "date"]
    
for fruit in fruits:
    if fruit == "cherry":
        break #Exits the loop if cherry is found
        print (fruit)
        
        print()
        
# using continue statement
for fruit in fruits:
    if fruit == "cherry":
        continue #skips cherry and moves to the iteration
        print (fruit)
        
        print()
        
# using pass statement
for fruit in fruits:
    if fruit == "cherry":
        pass # placeholder, no action is needed for cherry
        print (fruit)
        
        
        #while loop using break control statement
        count = 0
        while count < 5:
            print(count)
            count += 1
            if count == 3:
                break#exists the loop when the count is reached-3