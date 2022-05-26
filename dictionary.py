# Write a simple dictionary and print to the terminal
person = {
    'name': 'Offiong',
    'job': 'lawyer'
}
print(person) #{'name': 'Offiong', 'job': 'lawyer'}
print(person['name']) # Offiong

#delete a value from the dictionary
del person['job']
print(person) #{'name': 'Offiong'}

#add value to the dictionary
person['address'] = 'kubwa';
print(person) # {'name': 'Offiong', 'address': 'kubwa'}

# loop through the dictionary
# for key.value in person.items():
#     print('I have ' + name + 'relating with ' + Offiong)