import csv #import the csv file


def open_file():
    while True: #keep program in a while loop
        try:
            file = input("Enter name of file to open: ") #txt file is in repository
            with open(file, 'r') as search:
                txt = csv.reader(search, delimiter = ',')
                for row in txt:
                    words = list(row)
                    count = 1
                    #for every row in txt, save the words as a list? dict? set?
                    for word in words: # how do i iterate each word in a list?
                        if word in words:
                            count += 1
                        else:
                            count = 1
                        print(f'{word} occurs in this file {count} times')
                break
        except FileNotFoundError:
            print("ERROR could not find file")
        except IOError:
            print("An error occured while reading: ", file)


open_file()




