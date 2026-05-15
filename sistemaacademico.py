#dicionario com listas no lugar de valor para que seja possivel ter multiplos valores
dicionario = {
    "professor" : [],
    "curso" : [],
    "disciplina" : []

}
#sistema de Menu baseado em "match case" no caso o usuario precisa escrever exatamente o que ta no match e com isso ele será enviado a o proximo passo 
while True:
    print ("----bem vindo ao sistema academico----")
    print ("---- cadastrar novo curso----")
    print ("---- cadastrar novo professor---- ")
    print ("---- Cadastrar novo aluno")
    print ("---- cadastrar nota de alunos----")
    cadastro = str(input("cadastro..."))
    match cadastro:
        case "novo curso" | "Novo curso": # O "|" é basicamente um "and" só que funciona no match case, sim "and" não funciona no match case
            dicionario["curso"].append(input("olá qual novo curso gostaria de cadastrar?"))
            while True:
                dicionario["disciplina"].append(input("insira disciplina do novo curso"))
                continuar = (input("gostaria de adicionar uma nova disciplina?"))
                if continuar == "não" and "Não":
                    print (dicionario["disciplina"])
                    break
                elif continuar == "sim" and "Sim":
                    pass 
                else:
                    print("insira resposta valida")
        #aqui eu me perdi completamente já pois aqui já começa a precisar associar as listas
        case "novo professor" | "Novo professor":  
            dicionario["professor"].append(input("Seja bem vindo qual será o novo professor?"))
            for i in range (len(dicionario["curso"])):
                cursoresp = (input(dicionario["curso"(i)]))
            
            
        case "sair" | "Sair":
            break
#basicamente eu to tentando conseguir associar os valores das listas por exemplo associar grupo 1 de disciplina com curso x e etc. descobrindo isso o resto é EXTREMAMENTE mole



        
        