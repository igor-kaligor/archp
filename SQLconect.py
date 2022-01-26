import ssl
import psycopg2

#configurações
host = '35.184.224.12'
dbname = 'postgres'
user = 'postgres'
password = 'postgres123'
sslmode = 'require'

#String de Conexão
conn_String='host={0} user={1} dbname={2} password={3} sslmode={4}'.format(host, user, dbname, password, sslmode)
#print(conn_String)

class Conectar:

    def conexao(): 
        try:
            conn = psycopg2.connect(conn_String)
            return "conectado"
        except:
            return "Não foi possível estabelecer conexão"
    
    def query(query):
        try:
            conn = psycopg2.connect(conn_String)
            cursor = conn.cursor()
            print("Aguardando solicitação")
            cursor.execute(query)
            return cursor.fetchall()
        except:
            print("Não foi possível executar a solitação tente novamente")

    def insert(query,v1,v2):
        try:
            conn = psycopg2.connect(conn_String)
            cursor = conn.cursor()
            cursor.execute(query,(v1,v2,))
            conn.commit()
            print("Solicitação executada com sucesso")
        except:
            print("Não foi possível executar a solitação tente novamente")
    def upA(query,v1,v2):
        try:
            conn = psycopg2.connect(conn_String)
            cursor = conn.cursor()
            cursor.execute(query,(v1,v2,))
            conn.commit()
            print("Solicitação executada com sucesso")
        except:
            print("Não foi possível executar a solitação tente novamente")

    def insertNotas(query,v1,v2,v3,v4,v5,v6):
        try:
            conn = psycopg2.connect(conn_String)
            cursor = conn.cursor()
            cursor.execute(query,(v1,v2,v3,v4,v5,v6,))
            conn.commit()
            print("Solicitação executada com sucesso")
        except:
            print("Não foi possível executar a solitação tente novamente")

    def upN(query,v1,v2,v3,v4,v5):
        try:
            conn = psycopg2.connect(conn_String)
            cursor = conn.cursor()
            cursor.execute(query,(v1,v2,v3,v4,v5,))
            conn.commit()
            print("Solicitação executada com sucesso")
        except:
            print("Não foi possível executar a solitação tente novamente")
