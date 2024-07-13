def isRutRepeated(listRut,rut):
    for dictRut in listRut:
        if dictRut["rut"] == rut:
            return True
    return False

def getClientId(list,rut):
    for dictRut in list:
        if dictRut["rut"] == rut:
            return dictRut["id"]
    return -2

def isGestorRepeated(list,name):
    for dictGestor in list:
        if dictGestor["name"] == name:
            return True
    return False

def getGestorId(list,name):
    for dictGestor in list:
        if dictGestor["name"] == name:
            return dictGestor["id"]
    return -1