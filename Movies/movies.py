import csv

with open("telugu_movies.csv", "r") as movies_file:
    csv_reader = csv.reader(movies_file)
    print("Movie Details")
    print("---------------")
    for row in csv_reader:
        print("Movie Id : %s" % row[0])
        print("Movie Name : %s" % row[1])
        print("Director Name : %s" % row[2])
        print("Hero Name: %s" % row[3])
        print("Heroine Name: %s" % row[4])
        print("Movie Rating : %s" % row[5])
        print("Released Year : %s" % row[6])
        print("---------------")