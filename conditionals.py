# a simple CLI culculator that takes user input and performs addition, subtraction, division, multiplication and modulus operations

select_option = input('Want to perform a calculation? Choose yes or no \n')
if (select_option == 'yes'):
    num1 = int(input('Enter number: \n'))
    operator = input('Enter one operator between: +, -, x, / and % \n')
    num2 = int(input('Choose second number \n'))
    operator_list = ['+', '-', '/', 'x', '%']
    if (operator == operator_list[0]):
        result = num1 + num2
        print(result)
    elif (operator == operator_list[1]):
        result = num1 - num2
        print(result)
    elif (operator == operator_list[2]):
        result = num1 / num2
        print(result)
    elif (operator == operator_list[3]):
        result = num1 * num2
        print(result)
    elif (operator == operator_list[4]):
        result = num1 % num2
        print(result)
    else:
        print('invalid operation')
elif (select_option == 'no'):
    print('Have a nice day')
else:
    print('Invalid option')
    


#A simple program that takes username and password in order to allow the user sign in to the app/program
takeName = input('Enter your user name please \n')

nameList = ['Offiong', 'Wakilat']
password = 'Password'

if takeName in nameList:
    takePassword = input('Enter password please \n')

    if takePassword == password:
        print("You're succesfully logged in %s" % nameList)
        # Note that to concatenate the above string with the nameList, which is a list(array), you need to covert the list to a string. Hence the %s identifier/specifier.
    else:
        print('Incorrect password')

else:
    print('Error')



#A version of the password program that takes unique passwords for each user
takeName = input('Enter your user name please \n')

nameList = ['Offiong', 'Wakilat']
password = ['passwordOffiong', 'passwordWakilat']

if takeName in nameList:
    takePassword = input('Enter password please \n');
    userId = nameList.index(takeName) # That is the index of whatever name the user inputs

#The above user ID is going to be used to check the correct password below, considering that the index of each name is in the same index position as their unique password.

    if takePassword == password[userId]:
        print("You're succesfully logged in %s" % takeName)
        # Note that to concatenate the above string with the nameList, which is a list(array), you need to covert the list to a string. Hence the %s identifier/specifier.
    else:
        print('Incorrect password')

else:
    print('Error')



# This extension allows user to select an option, depending on the type of transaction they want to carry out

takeName = input('Enter your user name please \n')

nameList = ['Offiong', 'Wakilat']
password = ['passwordOffiong', 'passwordWakilat']

if takeName in nameList:
    takePassword = input('Enter password please \n');
    userId = nameList.index(takeName) # That is the index of whatever name the user inputs

#The above user ID is going to be used to check the correct password below, considering that the index of each name is in the same index position as their unique password.

    if takePassword == password[userId]:
        print("You're succesfully logged in %s" % takeName)
        # Note that to concatenate the above string with the nameList, which is a list(array), you need to covert the list to a string. Hence the %s identifier/specifier.
        print('These are the available options.')
        print('1. Withdrawal')
        print('2. Deposit')
        print('3. Transfer')
        print('4. Pay bills')

        selected_option = int(input('Please select an option \n')) #converted to integer sine input returns a string

        if (selected_option == 1):
            print('You selected %s' % selected_option)
        elif (selected_option == 2):
            print('You selected %s' % selected_option)
        elif (selected_option == 3):
            print('You selected %s' % selected_option)
        elif (selected_option == 4):
            print('You selected %s' % selected_option)
        else:
            print('Invalid option. Please try again')
            
    else:
        print('Incorrect password. Please try again.')

else:
    print('Error')



        
    