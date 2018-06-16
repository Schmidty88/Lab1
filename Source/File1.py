# Lab 1.1
# Take user input for password

user_pass = input("""

Enter a new password containing...
At least one upper(A),
one lower(a) case letter,
at least on character [$@!*], 
and at least one digit (0-9): """)

# Boolean variables for probing password, set condition for length and conditions to initiate checking other
# characters, digits, and case

contain_lower = False

contain_upper = False

contain_char = False

contain_digit = False

contain_length = True if len(user_pass) < 16 or len(user_pass) > 6 else False

# Once length is found true, loop initiates checking for other conditions

if contain_length is True:

    for u in user_pass:

        if u.isupper():

            contain_upper = True

        if u.islower():

            contain_lower = True

        if u.isdigit():

            contain_digit = True

        if u in "[$@!*]":

            contain_char = True

    else:
        print("The password has incorrect length, combination of digits, characters, or upper/lowercase letters...")

# loop has exited and if conditions are met the password is accepted, if statement prints line

if contain_digit and contain_char and contain_upper and contain_lower is True:

    print("Congrats! you have successfully created a password!")