import ssl
import psycopg2
from SQLconect import Conectar
from aluno import Aluno
from professor import Professor
Conectar.conexao()
def Qnotas(lista):
    
    print("__{0:^10}___{1:^20}___{2:^6}___{3:^6}___{4:^6}___{5:^6}___{6:^6}___{7:^11}__".format("__________","____________________","______","______","______","______","______","___________"))
    print("| {0:^10} | {1:^20} | {2:^6} | {3:^6} | {4:^6} | {5:^6} | {6:^6} | {7:^11} |".format("ID","NOME","NOTA 1","NOTA 2","NOTA 3","NOTA 4","MEDIA","SITUAÇÃO"))
    for i in range(len(lista)):
        sm=0
        md=0
        for g in range(2,6):
            sm=sm+QRY[i][g]
            #print(sm)
        md=sm/4
        if (md>=6):
            st="APROVADO"
        elif (md>=4 and md<6):
            st="RECUPERAÇÃO"
        elif(md<4):
            st="REPROVADO"
        print("+ {0:^10} + {1:^20} + {2:^6} + {3:^6} + {4:^6} + {5:^6} + {6:^6} + {7:^11} +".format("----------","--------------------","------","------","------","------","------","-----------"))
        print("| {0:^10} | {1:^20} | {2:^6} | {3:^6} | {4:^6} | {5:^6} | {6:^6} | {7:^11} |".format(QRY[i][0],QRY[i][1],QRY[i][2],QRY[i][3],QRY[i][4],QRY[i][5], md,st))
        
    print("|_{0:^10}_|_{1:^20}_|_{2:^6}_|_{3:^6}_|_{4:^6}_|_{5:^6}_|_{6:^6}_|_{7:^11}_|".format("__________","____________________","______","______","______","______","______","___________"))

def clear():
    input("\n\nAPERTE ENTER PARA CONTINUAR...")
    for y in range(80):
        print()

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("----------------------------------------------|PROGRAMA DESENVOLVIDO POR IGOR CASTRO|-----------------------------------------------------")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
clear()
k=3
while(k==3):
    g=int(input("SELECIONE UMA OPÇÃO: \n-DIGITE 1 PARA PROFESSOR- \n-DIGITE 0 PARA ALUNO- \n-DIGITE 2 PARA SAIR-\n"))
    if (g==0):
        p=input("Digite o codigo do aluno: ")
        QRY=[]
        QRY=Aluno.getNotas(p)
        Qnotas(QRY)
        clear()
    elif(g==1):
        op=int(input("Digite a opção:\n1- Visiualizar notas \n2- Registro de aluno \n3- Registro de notas\n"))
        if(op==1):
            QRY=[]
            QRY=Professor.getNotas()
            Qnotas(QRY)
            clear()

        elif(op==2):
            pp=int(input("Digite a opção:\n1- Cadastrar\n2- Atualizar\n"))
            if(pp==1):      
                CD=input("Digite o ID do aluno: \n")
                nome=input("Digite o nome do aluno: \n")
                Professor.setAluno(CD,nome)
                clear()
            elif(pp==2):      
                CD=input("Digite o ID do aluno: \n")   
                nome=input("Digite o novo nome do aluno: \n")
                Professor.upAluno(CD,nome)
                clear()
        elif(op==3):
            pp=int(input("Digite a opção:\n1- Cadastrar\n2- Atualizar\n"))
            if(pp==1):  
                CD=input("Digite o ID do Aluno: \n")
                arr=[]
                for k in range(4):
                    no=input("Digite a nota do aluno:\n") 
                    arr.append(no)    
                Professor.setNota(CD,CD,arr[0],arr[1],arr[2],arr[3])
                clear()
            elif(pp==2):
                CD=input("Digite o ID do aluno: \n")  
                arr=[] 
                for k in range(4):
                    no=input("Digite a nota do aluno:\n") 
                    arr.append(no)    
                Professor.upNota(CD,arr[0],arr[1],arr[2],arr[3])
                clear()
    else:
        k=4

clear()
exit()
#Aluno.getNotas()
