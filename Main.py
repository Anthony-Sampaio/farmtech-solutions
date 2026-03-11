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
        print("Você quer atualizar soja ou café?")
        print("1 - Soja")
        print("2 - Café")
        atualizacao = input("Digite um número: ")

        if atualizacao == "1":
            print("=== Lavouras de Soja ===")
            if len(soja) == 0:
                print("Nenhuma lavoura cadastrada.")
            else:
                for i in range(len(soja)):
                    print(i, soja[i])
                lavoura = int(input("Escolha uma lavoura: "))
                print("1 - Largura")
                print("2 - Comprimento")
                print("3 - Tipo do produto")
                print("4 - Quantidade de produto")
                campo = input("Escolha: ")
                if campo == "1":
                    while True:
                        try:
                            soja[lavoura]["Largura"] = float(input("Nova largura: "))
                            break
                        except ValueError:
                            print("Digite apenas números!")
                elif campo == "2":
                    while True:
                        try:
                            soja[lavoura]["Comprimento"] = float(input("Novo comprimento: "))
                            break
                        except ValueError:
                            print("Digite apenas números!")
                elif campo == "3":
                    soja[lavoura]["Tipo do produto"] = input("Novo produto: ")
                elif campo == "4":
                    while True:
                        try:
                            soja[lavoura]["Quantidade de produto"] = float(input("Nova quantidade: "))
                            break
                        except ValueError:
                            print("Digite apenas números!")
                print("Lavoura atualizada com sucesso!")

        elif atualizacao == "2":
            print("=== Lavouras de Café ===")
            if len(cafe) == 0:
                print("Nenhuma lavoura cadastrada.")
            else:
                for i in range(len(cafe)):
                    print(i, cafe[i])
                lavoura = int(input("Escolha uma lavoura: "))
                print("1 - Largura")
                print("2 - Comprimento")
                print("3 - Espaçamento")
                print("4 - Tipo do produto")
                print("5 - Quantidade de produto")
                campo = input("Escolha: ")
                if campo == "1":
                    while True:
                        try:
                            cafe[lavoura]["Largura"] = float(input("Nova largura: "))
                            break
                        except ValueError:
                            print("Digite apenas números!")
                elif campo == "2":
                    while True:
                        try:
                            cafe[lavoura]["Comprimento"] = float(input("Novo comprimento: "))
                            break
                        except ValueError:
                            print("Digite apenas números!")
                elif campo == "3":
                    while True:
                        try:
                            cafe[lavoura]["Espaçamento"] = float(input("Novo espaçamento: "))
                            break
                        except ValueError:
                            print("Digite apenas números!")
                elif campo == "4":
                    cafe[lavoura]["Tipo do Produto"] = input("Novo produto: ")
                elif campo == "5":
                    while True:
                        try:
                            cafe[lavoura]["Quantidade de Produto"] = float(input("Nova quantidade: "))
                            break
                        except ValueError:
                            print("Digite apenas números!")
                print("Lavoura atualizada com sucesso!")

    elif escolha ==  "4":
        print("Qual tipo de lavoura deseja deletar?")
        print("1 - Soja")
        print("2 - Café")
        deletar = input("Digite um número: ")

        if deletar == "1":
            print("=== Lavouras de Soja ===")
            if len(soja) == 0:
                print("Nenhuma lavoura cadastrada.")
            else:
                for i in range(len(soja)):
                    print(i, soja[i])
                lavoura = int(input("Escolha uma lavoura para deletar: "))
                soja.pop(lavoura)
                print("Lavoura deletada com sucesso!")

        elif deletar == "2":
            print("=== Lavouras de Café ===")
            if len(cafe) == 0:
                print("Nenhuma lavoura cadastrada.")
            else:
                for i in range(len(cafe)):
                    print(i, cafe[i])
                lavoura = int(input("Escolha uma lavoura para deletar: "))
                cafe.pop(lavoura)
                print("Lavoura deletada com sucesso!")