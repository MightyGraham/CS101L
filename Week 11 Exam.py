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
                    for word in words: # FIXME how do i iterate each word in a list and count how many times the occur?
                        if word in words:
                            count += 1
                        else:
                            count = 1
                        print(f'{word} occurs in this file {count} times')
                        if count == 1:
                            #print amount of words that only appear one time
                        if words.endswith('!')  or words.endswith('.'):
                            #figure out how many times punctuation is founded
                break
        except FileNotFoundError:
            print("ERROR could not find file")
        except IOError:
            print("An error occured while reading: ", file)


open_file()



