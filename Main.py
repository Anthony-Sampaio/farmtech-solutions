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
                largura = float(input("Largura do terreno: "))
                comprimento = float(input("Comprimento do terreno: "))
                produto = input("Tipo de produto disponível: ")
                qproduto = float(input("Quantidade de produto disponível: "))
                
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
                largura = float(input("Largura do terreno: "))
                comprimento = float(input("Comprimento do terreno: "))
                espacamento = float(input("Espaçamento das ruas: "))
                produto = input("Tipo de produto disponível: ")
                qproduto = float(input("Quantidade de produto disponível: "))

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
            