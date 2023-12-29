import csv
class excel:
    @classmethod
    def data(cls):
        with open("C:\\Users\\hp\\Downloads\\mac.csv", "r")as read:
            obj = csv.reader(read)
            for row in obj:
                print(row)



excel.data()
