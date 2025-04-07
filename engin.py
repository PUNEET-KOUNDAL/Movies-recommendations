import ast 



def convert(obj):
    L= [ ]
    for i in ast.literal_eval(obj) :
        L.append(i['name'])
    return L


def convert1(obj):
    L= [ ]
    count = 0
    for j in ast.literal_eval(obj) :
        if count != 4:
            L.append(j['name'])
            count += 1
        else :
            break
    return L


def fetchdirector(obj):
    L= [ ]
    for i in ast.literal_eval(obj) :
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L




