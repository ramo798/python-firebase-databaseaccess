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
def Periodd(a):
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
