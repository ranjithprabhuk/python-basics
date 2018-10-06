# Allow the user to give his input
print('Hi Developer!!\n')
user_input = input('Please enter you name: ')
print('\n\nHey ' + user_input + '!!, \nYou are a Python developer now!!')


# Determine the entered number is odd or even
print('\nHi, Lets find what number it is...')

user_entered_number = input('Enter a Number: ')
result = 'ODD'

if int(user_entered_number) % 2 == 0: # Its required to cast the value to integer because default input value will be string
    result = 'EVEN'


print('Hey, you have entered ' + user_entered_number + ' and its a "' + result + '" number')