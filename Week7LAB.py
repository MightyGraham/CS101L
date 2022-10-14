def vehfile():
    try:
        file = input("Enter the name of the input vehicle file (.txt)=> ")
        vehiclefile = open(file)
        print(vehiclefile.readline())#file need to be in the same directory as this program ^
        for line in vehiclefile:
            print(line)
        file2 = input("Enter the name of the output vehicle file (.txt)=> ")
        vehiclefile2 = open(file2)
        for line2 in vehiclefile:
            print(line2)
        vehiclesfile.close()
        vehiclefile2.close()
    except FileNotFoundError:
        print(f'Could not open file {file}')
        file = input("Now enter the name of the input vehicle file (.txt)=>")
    except IOError:
        print(f'There was an IOError {name}')
    

try:
    mpg = int(input("Enter the minimum miles-per-gallon => "))#ask for mpg 
    if 0 < mpg < 100: #instead of 'and', use this expression.
        print()
        vehfile()
    elif mpg > 100:
        print("ERROR: Fuel economy entered must be less than 100, try again.")
        mpg = int(input("Enter the minimum miles-per-gallon => "))
    elif mpg < 0:
        print("ERROR: Fuel economy entered must be greater than zero, try again.")
        mpg = int(input("Enter the minimum miles-per-gallon => "))
    else:
        print("ERROR: You must enter a number, try again.")
        mpg = int(input("Enter the minimum miles-per-gallon => "))
except ValueError: #execute this if input wasn't a number
    print()
    print("ERROR: You must enter a number, try again.")
    mpg = int(input("Enter the minimum miles-per-gallon => "))

    
    

    
    
