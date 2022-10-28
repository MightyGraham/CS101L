#imports
import csv


# functions
def month_from_number():
    while True:
        try:
            month = int(input("Enter month #: "))
            if month == 1:
                return "January"
            elif month == 2:
                return "February"
            elif month == 3:
                return "March"
            elif month == 4:
                return "April"
            elif month == 5:
                return "May"
            elif month == 6:
                return "June"
            elif month == 7:
                return "July"
            elif month == 8:
                return "August"
            elif month == 9:
                return "September"
            elif month == 10:
                return "October"
            elif month == 11:
                return "November"
            elif month == 12:
                return "December"
            else:
                print("Month Number must be 1 - 12")
        except ValueError:
            print("Error: Month must be a number")


def read_in_file():
    file = open("CrimeDataVS.csv", encoding="utf-8")
    file_csv = csv.reader(file)
    for line in file_csv:
        print(type(line))
        print(len(line))
        print(line[0])
        print(line)
    file.close()


def create_reported_date_dict():
    pass




def create_reported_month_dict():
    pass




def create_offense_dict():
    pass




if __name__ == "__main__":

    # Main program
    print("KCPD Crime Data")
    print(month_from_number())
    read_in_file()
    
    
