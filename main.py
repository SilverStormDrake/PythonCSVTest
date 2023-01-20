import csv

def main():
    with open('cards.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            print(', '.join(row))



if __name__ == "__main__":
    main()