#print a string that is repeated multiple times
voice = 'shout '
print(voice * 5)


#print the index of 'o' in the following string
string = 'hello'
print(string.index('o')) # 4

# print the index of the first 3 characters in the above string
# you do not need the index method
# you do not need parenthesis
# excludes the end index/index of the operand on the right, in this case, 3. so it will print 0-2
# if you do not specify an end index, it returns the entire string
# if you do not supply a start index, python will assume 0 as the start index

print(string[0:3]) # 'hel'
print(string[0:]) # 'hello'
print(string[:4]) # 'hell'


#FORMATTED STRINGS
# you use the f prefix to format strings
name = "Offiong"
surname = 'Ekpenyong'
message = f'{name} {surname} is a coder'

print(message) # Offiong Ekpenyong is a coder. Without the f prefix, it returns '{name} {surname} is a coder'


#STRING METHODS
# find the length of the following string:
find_length = 'hello world'
print(len(find_length)) #11

# convert the above string to uppercase
print(find_length.upper()) #HELLO WORD

# replace 'hello' with 'hi'
print(find_length.replace('hello', 'hi')) #hi world

# check if the string contains a certain word or character
print('good morning' in find_length) # false
print('hello' in find_length) # true
