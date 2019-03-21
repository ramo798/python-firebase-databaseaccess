import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'syllabus').document(u'観光政策')
doc_ref.set({
    u'tourism': True,
    u'economics': False,
    u'education': False,
    u'engineering': False,
    u'title': u'観光政策',
    u'teacher': u'青木義英',
    u'target': 1,
    u'term': False, #Trueが前期Falseが後期
    u'term-ex': False, #term-exception 通年などの例外
    u'day': 4, #日曜日が0
    u'period': 4, #何限目か

})
