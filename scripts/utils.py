def isRutRepeated(listRut,rut):
    for x in listRut:
        if x["rut"] == rut:
            return True
    return False

def getClientId(list,rut):
    for x in list:
        if x["rut"] == rut:
            return x["id"]
    return -2

def isGestorRepeated(list,name):
    for x in list:
        if x["name"] == name:
            return True
    return False

def getGestorId(list,name):
    for x in list:
        if x["name"] == name:
            return x["id"]
    return -1