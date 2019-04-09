def Majortou(a):
    if a == '観光学部':
        return True
    else:
        return False
def Majoreco(a):
    if a == '経済学部':
        return True
    else:
        return False
def Majoredu(a):
    if a == '教育学部':
        return True
    else:
        return False
def Majoreng(a):
    if a == 'システム工学部':
        return True
    else:
        return False
def Majorpan(a):
    if a == '教養科目':
        return True
    else:
        return False
def Targett(a):
    if a == '1年':
        return 1
    elif a == '2年':
        return 2
    elif a == '3年':
        return 3
    elif a == '4年':
        return 4
def Termm(a):
    if a == '前期':
        return True
    elif a == '後期':
        return False
    else:
        return False
def Terme(a):
    if a == '前期' or a == '後期':
        return False
    else:
        return True
def Dayday(a):
    if len(a) != 0:
        if a != '時間外':
            if a[0] == '月':
                return 1
            if a[0] == '火':
                return 2
            if a[0] == '水':
                return 3
            if a[0] == '木':
                return 4
            if a[0] == '金':
                return 5
            if a[0] == '土':
                return 6
            if a[0] == '日':
                return 0
        else: return 7
    else: return 8
def Periodd(a):
    if len(a) != 0:
        if a != '時間外':
            if a[1] == '１':
                return 1
            if a[1] == '２':
                return 2
            if a[1] == '３':
                return 3
            if a[1] == '４':
                return 4
            if a[1] == '５':
                return 5
            if a[1] == '６':
                return 6
        else: return 7
    else: return 8
def Daydayday(a):
    if len(a) != 0:
        day = a[0]
        tmp = 0
        if a != '時間外':
            if a[1] == '１':
                tmp = 1
                result = day + str(tmp)
                return result
            if a[1] == '２':
                tmp = 2
                result = day + str(tmp)
                return result
            if a[1] == '３':
                tmp = 3
                result = day + str(tmp)
                return result
            if a[1] == '４':
                tmp = 4
                result = day + str(tmp)
                return result
            if a[1] == '５':
                tmp = 5
                result = day + str(tmp)
                return result
            if a[1] == '６':
                tmp = 6
                result = day + str(tmp)
                return result
        else: return a
