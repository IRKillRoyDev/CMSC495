import csv

def main():
    with open('titles.csv', 'r') as homefile:
        for line in csv.DictReader(homefile): # DictReader is a reader that returns a dictionary from the source.
            for key in line:
                print(key + ': ' + line[key]) #Prints all the keys and values in the csv file in a certain format.
            print(line) #Prints the Dictionary entire line.
if __name__ == '__main__':
    main()
