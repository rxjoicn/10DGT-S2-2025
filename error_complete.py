# Error Checking
# Author : Josh Cheng
# Date: 22/10/2025
# Version 1.0
"""Changelog: """

# Code that tests whether a valid input is given
"""done = False
while not done:
    num = int(input("Please enter your value: "))
    done = True
    
print(f"The number that you entered is {num}.")"""


# Version 1.1
# Code that tests whether a valid input is given
# Use the try and except method to catch errors
"""Changelog:
Improved the code from version 1.1 """

"""done = False
while not done:
    try:
        num = int(input("Please enter a number: "))
        done = True
        
    except ValueError:
        print("The number you have entered is invalid. \n")
        done = False"""
        
# To create a function, start with the word def

'''def test_int_num():
    done = False
    while not done:
        try:
            num = int(input("Please enter a number (Interger): "))
            done = True
            
        except ValueError:
            print("The number you have entered is invalid.  /n")
            
    print(f"The number you have enteres is {num}. /n")'''
    
    
def valid_num(question,low, high):
    error = f"Whoops, that is not an interger between {low} and {high}. \n"
    
    while True: 
        try:
            response = int(input(question))
            
            if low <= response <= high:
                break
            
            else:
                print(error)
                
        except ValueError:
            print(error)
    return response

num_1 = valid_num("Enter a number between 1 and 10: ", 1,10)
print(f"You entered {num_1}\n")

num_2 = valid_num("Enter a number between 15 and 25: ",15,25)
print(f"You entered {num_2}\n")

num_3 = valid_num("Enter a number between 70 and 90: ",70,90)
print(f"You entered {num_3}\n")

multiply = num_1 * num_2 * num_3
print(f"Your three numbers multiplied together are equal to {multiply}\n")

sum = num_1 + num_2 + num_3
print(f"The total of {num_1}, {num_2}, and {num_3} is {sum}.\n")

if __name__ == "__main__":
    