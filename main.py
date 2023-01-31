import csv
import requests
import json



param ={
    "Gilded Drake"
}

def main():
    
    with open('cards.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
    #        print(', '.join(row))
    
    #response = requests.get()
    print(response.status_code)


if __name__ == "__main__":
    main()