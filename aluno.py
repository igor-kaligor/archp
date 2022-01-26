from ast import Try
from pyclbr import Class
import ssl
import psycopg2
from SQLconect import Conectar

class Aluno:
    def getNotas(id):
            qry= "SELECT aluno.id, aluno.nome, notas.n1, notas.n2, notas.n3, notas.n4 FROM aluno, notas WHERE aluno.id = notas.idaluno AND aluno.id ="+id
            Slect=Conectar.query(qry)
            return Slect        
