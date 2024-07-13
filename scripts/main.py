from config import config
import psycopg2
import sqlite3
from psycopg2 import Error
from utils import isRutRepeated,getClientId,isGestorRepeated,getGestorId

def main():
    clientStack =[]
    gestorStack=[]
    dbParams = config("creds")
    try:
        conSQL=sqlite3.connect("../db.sqlite3")
        conPg = psycopg2.connect(**dbParams)
        cursorSQL=conSQL.cursor()
        cursorPg = conPg.cursor()
        cursorPg.execute("SELECT * from tabla_cubo")
        row=cursorPg.fetchone()
        while row is not None:
            (nameUser,rut,nameGestor,monto,f_pago,abono)=row
            clientId=-1
            if isRutRepeated(clientStack,rut):
                clientId=getClientId(clientStack,rut)
            else:
                cursorSQL.execute('INSERT into clientes_cliente (name,rut) values (?,?)',(nameUser,rut))
                clientId = cursorSQL.lastrowid 
                clientStack.append({"rut":rut,"id":clientId})
            
            gestorId=-1
            if isGestorRepeated(gestorStack,nameGestor):
                gestorId=getGestorId(gestorStack,nameGestor)
            else:
                cursorSQL.execute('INSERT into gestores_gestor (name) values (?)',(nameGestor,))
                gestorId = cursorSQL.lastrowid 
                gestorStack.append({"name":nameGestor,"id":gestorId})

            cursorSQL.execute('INSERT into pagos_pago (f_pago,monto,abonos,cliente_id,gestor_id) values (?,?,?,?,?)',(f_pago,monto,abono,clientId,gestorId))
            row=cursorPg.fetchone()

        conSQL.commit() 
    except (Exception, Error) as error:
        print("Error: ", error)
    finally:
        if (conPg):
            conPg.close()

if __name__ == "__main__":
    main()
