from random import choice
from string import ascii_letters


print("Welcome to XXX User Registration Portal! Please enter the following details to set up your account.")
firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
emailId = input("Please enter your email address: ")
EmployeeDetails = [firstName, lastName, emailId]
print(EmployeeDetails)
apass = firstName[:2] + lastName[-2:] + "".join(choice(ascii_letters) for x in range(5))
print("Based on our password suggestion algorithm, your password is {apass}")

satisfied = input("Do you like the suggested password? Type Y/N.")
if satisfied.upper == "Y":
    print ("Registration successful. Thanks for registering! Your password is:", apass)
    break

elif satisfied.upper == "N":
    new_password = input("Please, enter a password that is at least 7 characters long.")
        while len(new_password) < 7:
             new_password = input("Please, enter a password that is at least 7 characters long.")
        else:
            apass = new_password
            print("Password accepted and registration is successful. Thanks for registering! Your password is {apass}")
            break
        
        elif user_password

lastUser = input("Are you the last user? Type y/n.")


EmployeeRecords ={
              'First name': firstName,
              'Last name': lastName,
              'Email address': emailId              
              }
 
list = [EmployeeRecords]
print(list)
