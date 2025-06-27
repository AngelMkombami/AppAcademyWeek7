#strings 

#message = 'Hello World'
#print(message)

#Advanced concepts - strings

message = ' Hello, World! '
print(message[0]) #indexing..it starts at zero
print(message[1])


print(len(message))#finding the length

print(message.strip()) #strip- Remove leading and trailing  whitepace

print(message.lower()) #convert all characters to lowercase

print(message.split(',')) #split the string into a list based on the comma 


#upper method
print(message.upper()) #convert all characters to uppercase

#replace method
text = "I like BMW"
new_text = text.replace("BMW", "TOYOTa")
print(new_text)  # Output: I like TOYOTA
    