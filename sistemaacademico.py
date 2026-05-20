#estou um pouco cansado vou fazer os slides e volto proxima semana com isso
#com listas no lugar de valor para que seja possivel ter multiplos valores
dicionario = {
    "professores" : [],
    "cursos" : [],
    "disciplinas" : [],
    "alunos" : []
}
#sistema de Menu baseado em "match case" no caso o usuario precisa escrever exatamente o que ta no match e com isso ele será enviado a o proximo passo 
while True:
    print ("----bem vindo ao sistema academico----")
    print ("---- cadastrar novo curso----")
    print ("---- cadastrar novo professor---- ")
    print ("---- Cadastrar novo aluno")
    print ("---- cadastrar nota dos alunos----")
    cadastro = str(input("cadastrar...")).lower()
    match cadastro:
        case "novo curso" | "curso": # O "|" é basicamente um "and" só que funciona no match case, sim "and" não funciona no match case
            dicionario["cursos"].append(input("olá qual novo curso gostaria de cadastrar?"))
            dicionario["disciplinas"].append(input("insira disciplina do novo curso"))
            # a linha abaixo basicamente transforma o ultimo index criado em uma lista
            dicionario["disciplinas"][-1] = [dicionario["disciplinas"][-1]]
            while True:
                continuardisc = (input("gostaria de adicionar uma nova disciplina?")).lower()
                if continuardisc == "não" and "n":
                    print(dicionario["cursos"][-1])
                    print(dicionario["disciplinas"][-1]) 
                    break
                elif continuardisc == "sim" and "s":
                    #se não tivessimos transformado "[-1]" em uma lista esse codigo abaixo não funcionaria
                    (dicionario["disciplinas"][-1]).append(input("insira nova disciplina"))
                else:
                    print("insira resposta valida")
        case "novo professor" | "professor":  
            dicionario["professores"].append(input("Seja bem vindo qual será o novo professor?"))
            #novamente transformando o ultimo valor criado em uma lista
            dicionario["professores"][-1] = [dicionario["professores"][-1]]
            while True:
                print (dicionario["cursos"])
                cursoesc = (input("insira curso que ele vai lecionar"))
                if cursoesc in (dicionario["cursos"]):
                    dicionario["professores"][-1].append(cursoesc)
                    cursoesc = (dicionario["cursos"]).index(cursoesc)
                    print(dicionario["disciplinas"][cursoesc])
                    discesc = (input("insira a disciplina que ele ira lecionar"))
                    dicionario["professores"][-1].append(discesc)
                    while True:
                        continuardisc2 = (input("ele lecionará outra disciplina?")).lower()
                        if continuardisc2 == "não" or continuardisc2 == "n":
                            break
                        elif continuardisc2 == "sim" or continuardisc2 == "s":
                            dicionario["professores"][-1].append(input("insira mais uma disciplina"))
                        else:
                            print("insira resposta valida")
                print(dicionario["professores"])
                break
            else:
                print("insira resposta valida")
        case "novo aluno" | "aluno":
            dicionario["alunos"].append(input("qual será o novo aluno?"))
            dicionario["alunos"][-1] = [dicionario["alunos"][-1]]
            print(dicionario["cursos"])
            materiacursada = (input("qual materia ele ira cursar"))
            while True:
                if materiacursada in (dicionario["cursos"]):
                    dicionario["alunos"][-1].append(materiacursada)
                    print(dicionario["alunos"][-1])
                    break
                else:
                    print("insira resposta valida")
#em contrução                                
        case "nota dos alunos" | "notas":
            cursoava = (input("insira o curso onde será manuseado as notas"))
            if cursoava in (dicionario["cursos"]):
                if cursoava in dicionario["alunos"]:
                    print(dicionario["alunos"][[]])
            else:
                print("insira resposta valida") 
        case "sair" | "s":
            break
#"(dicionario["cursos"][(dicionario["cursos"].index(cursoava))])." maneira de usar index sem saber o index



        
        
