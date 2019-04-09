import firebase_admin
from module import Majoreco,Majoredu,Majortou,Majoreng,Targett,Termm,Terme,Dayday,Periodd,Daydayday,Majorpan
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('key2.json')
firebase_admin.initialize_app(cred)
db = firestore.client()




import csv
with open('kkk.csv', 'r') as f:
    reader = csv.reader(f)
    no = 1

    for row in reader:
        tou = Majortou(row[0])
        eco = Majoreco(row[0])
        edu = Majoredu(row[0])
        eng = Majoreng(row[0])
        pan = Majorpan(row[0])
        title = row[1]
        teacher = row[2]
        target = row[3]
        day = Daydayday(row[4])
        term = row[5]
        kubun = row[6]
        kazu = row[7]
        overview = row[8]
        goal = row[9]
        evaluation = row[10]
        text = row[11]
        text2 = row[12]
        message = row[13]
        learning = row[14]

        doc_ref = db.collection(u'syllabus-comp').document(title)
        data = {
            u'tourism': tou,#trueの場合その学部の授業
            u'economics': eco,#trueの場合その学部の授業
            u'education': edu,#trueの場合その学部の授業
            u'engineering': eng,#trueの場合その学部の授業
            u'culture': pan,
            u'no': no, #通し番号
            u'title': title, #授業名
            u'teacher': teacher, #教師の名前
            u'target': target,  #何回生向けか
            u'day': day,#空欄は8
            u'term': term, #Trueが前期Falseが後期
            u'kubun': kubun, #
            u'kazu': kazu, #単位数
            u'overview': overview,#概要
            u'goal': goal,#目標
            u'evaluation': evaluation,#評価方法
            u'text': text,#教科書
            u'text2': text2,#参考文献
            u'message': message,#メッセージ
            u'learning': learning,#学習方法
        }
        doc_ref.set(data) #送信
        print(no)
        no = no + 1


f.close()
