import csv
from datetime import datetime


#escrevam o cógido abaixo do comentário com seu nome
#variaveis: tarefa, descricao, data, tipodetarefa
#objeto = agenda
#funcoes = imprimir_atrasadas(), cadastrar_tarefa(), editar_tarefa(), criar_arquivo(), ler_csv()

#DaNasser



#Vitotoso



#GitHug-o
def imprimir_atrasadas(agenda):
    for tarefa in agenda:
        if agenda['Data'] > datetime.now():
            print(tarefa)
        else:
            print("Não há atividades atrasadas!")
    criar_arquivo()


#BernardoGuerino



