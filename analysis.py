from textblob import TextBlob
import csv
import string

def main():
    printable = set(string.printable)
    reader = csv.reader(open('./data/5_10-6_1.csv', 'rb'))
    fd = open("out.csv", "wb+")
    writer = csv.writer(fd)
    header = reader.next()
    header.append('sentiment')
    writer.writerow(header)
    # count = 0
    for row in reader:
        # print count
        # count = count + 1
        text = row[2]
        cleantext = filter(lambda x: x in printable, text)
        blob = TextBlob(cleantext)
        row.append(blob.sentiment[0])
        writer.writerow(row)
    fd.close()


if __name__ == '__main__':
    main()



