import firebase_admin
from module import Majoreco,Majoredu,Majortou,Majoreng,Targett,Termm,Terme,Dayday,Periodd
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()




import csv
with open('list0.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        tou = Majortou(row[0])
        eco = Majoreco(row[0])
        edu = Majoredu(row[0])
        eng = Majoreng(row[0])
        title = row[1]
        teacher = row[2]
        target = Targett(row[3])
        term = Termm(row[4])
        termex = Terme(row[4])
        day = Dayday(row[5])
        period = Periodd(row[5])

        doc_ref = db.collection(u'syllabus').document(title)
        data = {
            u'tourism': tou,
            u'economics': eco,
            u'education': edu,
            u'engineering': eng,
            u'title': title,
            u'teacher': teacher,
            u'target': target,
            u'term': term, #Trueが前期Falseが後期
            u'term-ex': termex, #term-exception 通年などの例外
            u'day': day, #日曜日が0 時間外は7
            u'period': period, #何限目か 時間外は7
        }
        doc_ref.set(data) #送信


f.close()
