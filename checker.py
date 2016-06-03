from textblob import TextBlob
import csv
import string

def main():


    reader1 = csv.reader(open('./out.csv', 'rb'))
    data1 = list(reader1)

    for d in data1:
        print d


if __name__ == '__main__':
    main()



