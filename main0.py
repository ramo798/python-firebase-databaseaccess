import firebase_admin
from module import Majoreco,Majoredu,Majortou,Majoreng,Targett,Termm,Terme,Dayday,Periodd
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('key2.json')
firebase_admin.initialize_app(cred)
db = firestore.client()




import csv
with open('somesome.csv', 'r') as f:
    reader = csv.reader(f)
    no = 1

    for row in reader:
        title = row[0]
        teacher = row[1]
        target = row[2]
        day = Dayday(row[3])
        period = Periodd(row[3])
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

        doc_ref = db.collection(u'syllabus-detail').document(title)
        data = {
            u'no': no, #通し番号
            u'title': title, #授業名
            u'teacher': teacher, #教師の名前
            u'target': target,  #何回生向けか
            u'day': day,#日曜日が0 時間外は7 空欄は8
            u'period': period, #何限目か 時間外は7 空欄は8
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
