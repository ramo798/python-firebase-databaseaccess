import firebase_admin
from module import Majoreco,Majoredu,Majortou,Majoreng,Targett,Termm,Terme,Dayday,Periodd
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('key2.json')
firebase_admin.initialize_app(cred)
db = firestore.client()




import csv
with open('somesome0.csv', 'r') as f:
    reader = csv.reader(f)


    for row in reader:
        title = row[0]
        teacher = row[1]
        target = row[2]
        day = row[3]
        term = row[4]
        kubun = row[5]
        kazu = row[6]
        overview = row[7]
        goal = row[8]
        evaluation = row[9]
        text = row[10]
        text2 = row[11]
        message = row[12]
        learning = row[13]

        doc_ref = db.collection(u'syllabuss51651465').document(title)
        data = {
            u'title': title,
            u'teacher': teacher,
            u'target': target,
            u'day': day,
            u'term': term, #Trueが前期Falseが後期
            u'kubun': kubun,
            u'kazu': kazu,
            u'overview': overview,
            u'goal': goal,
            u'evaluation': evaluation,
            u'text': text,
            u'text2': text2,
            u'message': message,
            u'learning': learning,
        }
        doc_ref.set(data) #送信


f.close()
