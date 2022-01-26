import ssl
import psycopg2
from SQLconect import Conectar

class Professor:
    def getNotas():
        qry= "SELECT aluno.id, aluno.nome, notas.n1, notas.n2, notas.n3, notas.n4 FROM aluno, notas WHERE aluno.id = notas.idaluno "
        Slect=Conectar.query(qry)
        return Slect
    def setAluno(ID,nome):
        qry = "INSERT INTO aluno (id,nome) VALUES (%s,%s);"
        Ist=Conectar.insert(qry,ID,nome)
        print("Aluno cadastrado com Sucesso!!")
    def upAluno(ID,nome):
        qry = "UPDATE aluno SET nome=%s WHERE id=%s;"
        Ist=Conectar.upA(qry,nome,ID)
        print("Aluno alterado com Sucesso!!")
    def setNota(ID,idAluno,v1,v2,v3,v4):
        qry = "INSERT INTO notas (id,idaluno,n1,n2,n3,n4) VALUES (%s,%s,%s,%s,%s,%s);"
        Ist=Conectar.insertNotas(qry,ID,idAluno,v1,v2,v3,v4)
        print("Aluno cadastrado com Sucesso!!")
    def upNota(ID,v1,v2,v3,v4):
        qry = "UPDATE notas SET n1=%s,n2=%s,n3=%s,n4=%s WHERE id=%s;"
        Ist=Conectar.upN(qry,v1,v2,v3,v4,ID)
        print("Aluno cadastrado com Sucesso!!")
    