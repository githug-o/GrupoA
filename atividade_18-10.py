import csv


#escrevam o cógido abaixo do comentário com seu nome
#variaveis: tarefa, descricao, data, tipodetarefa
#objeto = agenda
#funcoes = imprimir_atrasadas(), cadastrar_tarefa(), editar_tarefa(), criar_arquivo(), ler_csv()

#DaNasser



#Vitotoso



#GitHug-o



#BernardoGuerino
def cadastrar_tarefa(agenda)
    tarefa= {
        'Tarefa' : input("Digite a tarefa que teve ser realizada "),
        'Lista' : input("Lista : "),
        'Data' : input("Digite a data "),
        'Status' : "Pendente"
    }
    agenda.append(tarefa)
    criar_csv()
    print("")
    print("Tarefa adicionada")
    print("")
    



