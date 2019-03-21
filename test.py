import firebase_admin
from module import Majoreco,Majoredu,Majortou,Majoreng,Targett,Termm,Terme,Dayday,Periodd
from firebase_admin import credentials
from firebase_admin import firestore






import csv
with open('list0.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:

        day = Dayday(row[5])
        period = Periodd(row[5])

        print(day)
        #print(period)



f.close()
