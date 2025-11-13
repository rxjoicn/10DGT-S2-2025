# Checks whether if the number entered is a positive integer greater than zero
def valid_num(dimension,min):
    error = f"Whoops, that is not an interger greater than {min}. \n"
    
    while True: 
        try:
            response = float(input(dimension))
            
            if min < response:
                break
            
            else:
                print(error)
                
        except ValueError:
            print(error)
    return response

# A variable set to being empty so i can use it later for the loop
keep_going = ""

# Asks the user for values (Width, Length, Cost, etc.)
while keep_going == "":
    width = valid_num("Enter the width as a positve number greater than 0: ", 0)
    print(f"You have entered the width as: {width}m")
    print()
    

    length = valid_num("Enter the length as a positve number greater than 0: ", 0)
    print(f"You have entered the length as: {length}m")
    print()
        
    cost = valid_num("Enter the cost/m for the fence as a positive number greater than 0: ",0)
    print(f"You have entered the cost/m as: ${cost}")
    print()

    perimeter = 2 * float(length + width)
    print(f"The perimeter of the shape you have entered is {perimeter}m.")
    print()
        
    total_cost = float(perimeter * cost)
    print(f"The total cost of fencing for your entered values is ${total_cost}.")
    print()
    
    # Asks the user if they want to run the program again by pressing enter or no by pressing any other key
    keep_going = input("Do you want to run it again? <ENTER> - Yes, <ANY OTHER KEY> - EXIT: ")
print("Thanks for using, have a good day!")
            
        
    
    
    




