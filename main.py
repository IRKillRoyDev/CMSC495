import csv

def main():
    with open('titles.csv', 'r') as homefile:
        print(sum([len(homefile[x]) for x in homefile if isinstance(homefile[x], list)]))

if __name__ == '__main__':
    main()
