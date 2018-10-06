# Variables in Python

# Integers Float and String variables
experience = 6
height = 5.8
weight = 65
height_unit = "inch"
weight_unit = "kg"
experience_unit = "years"

print('Hey Developer!!\n\n\nYou wanna know about me')
print('\n\t My Experience: ' + str(experience) + ' ' + experience_unit)
print('\n\t My Height: ' + str(height) + ' ' + height_unit)
print('\n\t My Weight: ' + str(weight) + ' ' + weight_unit)


# Delete a varible in python
del experience
del height
del weight

del height_unit, weight_unit, experience_unit

input('\nEnter to continue to learn about Strings...\n')

# If you try to print the below lines, you will get exception as experience is deleted - enable and try it out
# print('\n\t My Experience: ' + str(experience) + ' ' + experience_unit)


# Strings and String Manipaulation

print ('\n Hey Developer, Lets do something with the string\n')
user_input = input('\t Enter a string: ')
user_input_length = len(user_input)

print('Hey, you have entered: ' + user_input + ' and its length is ' + str(user_input_length))

if user_input_length > 5:
    print ('First character you have entered: '+ user_input[0])
    print('Hey, let me print 3rd to 5th letter: '+ user_input[2:5])
    print('Hey, lets print all character from 3rd position: '+ user_input[2:])
    print('Hey, How about printing the value twice: '+ user_input * 2)

del user_input, user_input_length
input('\nEnter to continue to learn about Lists...\n')

# List

print ('\n Hey Developer, Now we are going to deal with Lists\n')
user_list = ['developer', 'tester', 'manager', 'lead', 'analyst', 'product owner']


print(user_list)
print('We have the above elements in the list:\n')

print(user_list[0])
print('First element in the list:\n')

print(user_list[2:5])
print('Hey, Printed 3rd to 5th elements:\n')

print(user_list[2:])
print('Hey, Printed all elements from 3rd position:\n')

print(user_list * 2)
print('Hey, How about printing the elements twice:\n')

input('\nEnter to continue to learn about Tuples...\n')

print(""" A tuple is another sequence data type that is similar to the list.
A tuple consists of a number of values separated by commas.
Unlike lists, however, tuples are enclosed within parentheses.

The main differences between lists and tuples are:
Lists are enclosed in brackets ( [ ] ) and
their elements and size can be changed,
while tuples are enclosed in parentheses ( ( ) ) and cannot be updated.
Tuples can be thought of as read-only lists.""")

input('\nEnter to continue to learn about Dictionary...\n')

print('Hey developer, enter the following the info please\n')
userName = input('May I know your name: ')
userExperience = input('May I know your experience: ')
userAge = input('May I know your age: ')

userInformation = {'name': userName, 'experience': userExperience, 'age': userAge}

print('\n')
print(userInformation)
print('Above user information is available in the dictionary\n')

print('Username of the user: ' + userInformation['name'])
