print("Olá, vou te ajudar com a lavoura!")

soja = []
cafe = []

while True:
    print("=== FarmTech Solutions ===")
    print("1 - Cadastrar lavoura")
    print("2 - Ver lavouras cadastradas")
    print("3 - Atualizar lavoura")
    print("4 - Deletar lavoura")
    print("5 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
            print("1 - Soja")
            print("2 - Café")
            plantio = input("O que você pretende plantar? ")


            if plantio == "1":
                while True:
                    try:
                        largura = float(input("Largura do terreno: "))
                        break
                    except ValueError:
                        print("Digite apenas números, sem unidades de medida!")
                while True:
                    try:
                        comprimento = float(input("Comprimento do terreno: "))
                        break
                    except ValueError:
                        print("Digite apenas números, sem unidades de medida!")
                produto = input("Tipo de produto disponível: ")
                while True:
                    try:
                        qproduto = float(input("Quantidade de produto disponível: "))
                        break
                    except ValueError:
                        print("Digite apenas números, sem unidades de medida!")
                    
                area = largura * comprimento
                insumo = qproduto * area

                soja.append({
                "Largura":largura,
                "Comprimento": comprimento,
                "Tipo do produto": produto,
                "Quantidade de produto": qproduto,
                "Área de plantio": area,
                "Insumo": insumo,
                })
                print("Lavoura cadastrada com sucesso!")
                    

            elif plantio == "2":
                while True:
                    try:
                        largura = float(input("Largura do terreno: "))
                        break
                    except ValueError:
                        print("Digite apenas números, sem unidades de medida!")
                while True:
                    try:
                        comprimento = float(input("Comprimento do terreno: "))
                        break
                    except ValueError:
                        print("Digite apenas números, sem unidades de medida!")
                while True:
                    try:
                        espacamento = float(input("Espaçamento das ruas: "))
                        break
                    except ValueError:
                        print("Digite apenas números, sem unidades de medida!")
                produto = input("Tipo de produto disponível: ")
                while True:
                    try:
                        qproduto = float(input("Quantidade de produto disponível: "))
                        break
                    except ValueError:
                        print("Digite apenas números, sem unidades de medida!")

                area = largura * comprimento
                nruas = largura / espacamento
                insumo = qproduto * comprimento * nruas

                cafe.append({
                "Largura":largura,
                "Comprimento": comprimento,
                "Espaçamento": espacamento,
                "Tipo do Produto": produto,
                "Quantidade de Produto": qproduto,
                "Área de plantio": area,
                "Número de ruas": nruas,
                "Insumo": insumo,
                })
                print("Lavoura cadastrada com sucesso!")
                

            else:
                print("Resposta inválida.")


    elif escolha == "2":
            print("=== Lavouras de Soja ===")
            if len(soja) == 0:
                print("Nenhuma lavoura cadastrada.")
            else:
                for i in range(len(soja)):
                    print(i, soja[i])

            print("=== Lavouras de Café ===")
            if len(cafe) == 0:
                print("Nenhuma lavoura cadastrada.")
            else:
                for i in range(len(cafe)):
                    print(i, cafe[i])

            input("Pressione Enter para voltar...")

    elif escolha == "3":
        print("Você quer atualizar soja ou café??")
