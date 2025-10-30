def valid_num(width,low):
    error = f"Whoops, that is not an interger greater than {low}. \n"
    
    while True: 
        try:
            response = float(input(width))
            
            if low <= response:
                break
            
            else:
                print(error)
                
        except ValueError:
            print(error)
    return response

def main():
    while True:
        width = valid_num("Enter the width as a positve number greater than 0: ", 0)
        print(f"You have entered the width as: {width}")

        height = valid_num("Enter the height as a positve number greater than 0: ", 0)
        print(f"You have entered the height as: {height}")

        perimeter = 2 * float(height + width)
        print(f"The perimeter of the shape you have entered is {perimeter}.")

        area = float(height * width)
        print(f"The area of the shape you have entered is {area}. ")

        again = str(input((f"Do you want to run it again? <ANY KEY> - Yes, <N> - No: ")).lower())
        if again == "n":
          quit()
    
main() 
        
    
    
    




