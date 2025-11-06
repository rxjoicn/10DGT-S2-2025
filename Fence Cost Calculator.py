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

keep_going = ""
while keep_going == "":
    width = valid_num("Enter the width as a positve number greater than 0: ", 0)
    print(f"You have entered the width as: {width}m")
    print()
    

    length = valid_num("Enter the length as a positve number greater than 0: ", 0)
    print(f"You have entered the length as: {length}m")
    print()
        
    cost = valid_num("Enter the cost/m for the fence as a positive number greater than 0: ",0)
    print()

    perimeter = 2 * float(length + width)
    print(f"The perimeter of the shape you have entered is {perimeter}m.")
    print()
        
    total_cost = float(perimeter * cost)
    print(f"The total cost of fencing for your entered values is ${total_cost}.")
    print()

    keep_going = input("Do you want to run it again? <ENTER> - Yes, <ANY OTHER KEY> - EXIT: ")
print("Thanks for using, have a good day!")
            
        
    
    
    




