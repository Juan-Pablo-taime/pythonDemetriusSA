#dicionario com listas no lugar de valor para que seja possivel ter multiplos valores
dicionario = {
    "professores" : [],
    "cursos" : [],
    "disciplinas" : [],
    "banco de dados" : []
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
            dicionario["cursos"].append(input("olá qual novo curso gostaria de cadastrar?"))
            dicionario["disciplinas"].append(input("insira disciplina do novo curso"))
            # a linha abaixo basicamente transforma o ultimo index criado em uma lista
            dicionario["disciplinas"][-1] = [dicionario["disciplinas"][-1]]
            while True:
                continuar = (input("gostaria de adicionar uma nova disciplina?"))
                if continuar == "não" and "Não":
                    print(dicionario["cursos"][-1])
                    print(dicionario["disciplinas"][-1]) 
                    break
                elif continuar == "sim" and "Sim":
                    #se não tivessimos transformado "[-1]" em uma lista esse codigo abaixo não funcionaria
                    (dicionario["disciplinas"][-1]).append(input("insira nova disciplina"))
                else:
                    print("insira resposta valida")
        case "novo professor" | "Novo professor":  
            dicionario["professores"].append(input("Seja bem vindo qual será o novo professor?"))
            #novamente transformando o ultimo valor criado em uma lista
            dicionario["professores"][-1] = [dicionario["professores"][-1]]
            #parte abaixo esta em construção ainda
            while True:
                print (dicionario["cursos"])
                cursoesc = (input("insira curso que ele vai lecionar"))
                if cursoesc in (dicionario["cursos"]):
                    cursoesc = (dicionario["cursos"]).index(cursoesc)

                    

                    print(cursoesc)
                    break
                else:
                    print("insira resposta valida")
            

                
                
                
        case "sair" | "Sair":
            break
#basicamente eu to tentando conseguir associar os valores das listas por exemplo associar grupo 1 de disciplina com curso x e etc. descobrindo isso o resto é EXTREMAMENTE mole



        
        