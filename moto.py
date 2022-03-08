class Cliente():
    indice = 0

    def __init__ (self, nome, id, contato):
        self.n_reg = Cliente.indice + 1
        self.nome = nome.title().strip()
        self.id = id.strip()
        self.contato = contato
        self.compra = []
        Cliente.indice += 1

    def __repr__ (self):
        return f"{self.n_reg} » \n Nome: {self.nome} \n Identificação: {self.id} \n Contato: {self.contato} \n ----------- \n"


class Motocicleta():
    quant = 0

    def __init__ (self, modelo, ano, valor, unidades):
        self.indice = Motocicleta.quant + 1
        self.modelo = modelo.title().strip()
        self.ano = int(ano)
        self.valor = int(valor)
        self.valor_de_venda = self.valor * 1.2
        self.estoque = int(unidades)
        Motocicleta.quant += 1

    def __repr__ (self):
        return f"\n #{self.indice} » \n Modelo: {self.modelo} \n Ano: {self.ano} \n " \
               f"Valor de Venda: R${self.valor_de_venda:.2f} \n Estoque = {self.estoque}" \
               f"\n----------------"


class Venda():
    registro = 0
    total_em_vendas = 0

    def __init__ (self, client, prod, parcelas):
        self.registro = Venda.registro + 1
        self.cliente = client
        self.produto = prod
        self.valor = 0
        for i in prod:
            self.valor += i.valor_de_venda
            Venda.total_em_vendas += i.valor_de_venda
        self.prestacoes = parcelas
        self.valor_parcelas = self.valor / parcelas * 1.1
        Venda.registro += 1

    def __repr__ (self):
        return f"\n ««««««««««««««««««*»»»»»»»»»»»»»»»»» \n " \
               f"|||| Venda #{self.registro} |||| \n " \
               f"Comprador: {self.cliente} \n " \
               f"Produtos: {self.produto} \n " \
               f"Quantidade de Prestações: {self.prestacoes} \n " \
               f"Valor dos Produtos: R${self.valor:.2f} \n " \
               f"Valor das Prestações: R${self.valor_parcelas:.2f} \n " \
               f"Valor final: R${self.valor_parcelas * self.prestacoes:.2f} \n " \
               f"««««««««««««««««««*»»»»»»»»»»»»»»»»» \n"


def reload (file_name):
    try:
        f = open(file_name, "x")
        f.close()
    except:
        with open(file_name, "r+") as file:
            lista = []
            lista_2 = []
            load = []
            new = False
            inlist = False

            for line in file:
                if line == "++ \n":
                    new = True
                    load = []
                    lista.append(load)

                elif line == '@ \n':
                    inlist = not inlist
                    lista_2 = []
                    if inlist:
                        load.append(lista_2)
                    continue

                else:
                    new = False
                    lista_2.append(line.strip())
                if new == False and inlist == False:
                    load.append(line.strip())

            # print("\n++++++++++++")
            # print("Linha: ", line)
            # print("new é", new)
            # print("inlist é", inlist)
            # print("lista_2 é", lista_2)
            # print("Load é", load)
            # print("lista é ", lista)
            return lista


def save (file_name, info):
    with open(file_name, "w+") as data:
        for inst in info:
            data.write("++ \n")

            '''for atr in inst:
                print("O Arg é ", atr)
                print("a linha é ", inst)
                print("tipo do atr ",type(atr))
                print("------")
                if type(atr) == str:
                    data.write(str(atr) + "\n")
                elif type(atr) == list:
                    data.write('@ \n')

                    for i in atr:
                        print("Iteracao em atr: ", i )
                        data.write(i + "\n")
                    data.write('@ \n')
                else:
                    raise TypeError
            print("a linha é:", inst)'''


#
arquivos = {"clientes": "dados_clientes.txt", "motocicletas": "dados_motocicletas.txt", "vendas": "dados_vendas.txt"}

clientes_1 = reload(arquivos["clientes"]) or []
motos_1 = reload(arquivos["motocicletas"]) or []
vendas_1 = reload(arquivos["vendas"]) or []

CLIENTES = [Cliente(cl[0], cl[1], cl[2]) for cl in clientes_1]  # [Cliente("nom", "ident", "telef"), Cliente("Teste 2",
# "Id Teste", "Telef Teste")]
cliente_dic = {cl.n_reg: cl for cl in CLIENTES}

MOTOCICLETAS = [Motocicleta(mt[0], mt[1], int(mt[2]), int(mt[3])) for mt in
                motos_1]  # [Motocicleta("Kawasaki", "2000", 43580, 3), Motocicleta("Kiwi", "2010", 48580, 5)]
moto_dic = {mt.indice: mt for mt in MOTOCICLETAS}

VENDAS = [Venda(cliente_dic[int(vn[0])], [moto_dic[int(mt)] for mt in vn[1]], int(vn[2])) for vn in
          vendas_1]  # [Venda(CLIENTES[0], [MOTOCICLETAS[0], MOTOCICLETAS[1]], 3),Venda(CLIENTES[1], [MOTOCICLETAS[0], MOTOCICLETAS[1]], 80)]

DATA_C = [[str(c.nome), str(c.id), str(c.contato)] for c in CLIENTES]
DATA_M = [[m.modelo, str(m.ano), str(m.valor), str(m.estoque)] for m in MOTOCICLETAS]
DATA_V = [[str(v.cliente.n_reg), [str(m.indice) for m in v.produto], str(v.prestacoes)] for v in VENDAS]

save_cl = save(arquivos["clientes"], DATA_C)
save_mt = save(arquivos["motocicletas"], DATA_M)
save_vn = save(arquivos["vendas"], DATA_V)


def cabeçalho (var):
    print(f"\n Aluguel motos --- {var} ---")


def comando (op):
    run = True
    while run == True:
        try:
            COMANDO = int(input("Selecione: "))
        except TypeError:
            print("Apenas numeros inteiros!")
        except ValueError:
            print("Por favor digite um número!")
        else:
            if COMANDO < 1 or COMANDO > len(op) + 1:
                print("Opção inválida!")


            else:
                run = False
                print("")
                if COMANDO == len(op) + 1:
                    print('Finalizando Programa')
                    break
                else:
                    op[COMANDO - 1]()


def menuprinc ():
    def bin_choice (title):
        print(title)
        repeat = True
        while repeat:
            try:
                choice = str(input('s/n: '))
                if choice == "":
                    print("Comando inválido!\n")
                elif choice in 'sS':
                    choice = True
                    return choice
                elif choice in 'Nn':
                    choice = False
                    return choice
                else:
                    print("Comando inválido!\n")
            except:
                print("Comando inválido!")

    def venda_menu ():

        def reg_venda ():
            cabeçalho("Registro de Vendas")
            print(VENDAS)
            print("\n 1) Voltar \n 2) Sair do Programa", "\n")
            comando([menuprinc])

        def nov_venda ():
            produtos = [[]]
            repeat = True
            counter = 2
            if MOTOCICLETAS == []:
                print("Nenhum produto cadastrado!")
                print("\n 1) Voltar \n 2) Sair do Programa", "\n")
                comando([menuprinc])
            if CLIENTES == []:
                print("Nenhum Cliente Cadastrado!")
                print("\n 1) Voltar \n 2) Sair do Programa", "\n")
                comando([menuprinc])

            cabeçalho("Nova Venda")
            print('Selecione o(s) produtos da venda: ')
            print("\n -- Registro de Produtos -- \n")
            print(MOTOCICLETAS)
            print('\n')
            produtos[0].append(MOTOCICLETAS[int(input('Digite o Registro do 1° Produto: ')) - 1])

            while repeat:
                repeat = bin_choice('Incluir outro produto? \n')
                if repeat == True:
                    produtos[0].append(MOTOCICLETAS[int(input(f'Digite o Registro do {counter}° Produto: ')) - 1])
                    counter += 1
                else:
                    break

            print('\n ========== \n')

            print('Selecione o Cliente: ')
            print("\n -- Registro de Clientes -- \n")
            print(CLIENTES)
            print('\n')
            produtos.append(CLIENTES[1 - int(input('Digite o Registro do Cliente: '))])

            print('\n ========== \n')

            print("\n Digite o numero de parcelas \n")
            parcelas = int(input(' Parcelas: '))

            print('\n -- CONFIRMAÇÃO DE VENDA -- \n')

            print(' - PRODUTO(S) --------- \n ')
            print(produtos[0])
            print('\n - CLIENTE --------- \n ')
            print(produtos[1])

            print('\n Parcelas: ', parcelas)

            repeat = bin_choice('Confirma os dados da venda?')
            if repeat:
                VENDAS.append(Venda(produtos[1], produtos[0], parcelas))
                print(VENDAS[-1])

                DATA_V = [[str(v.cliente.n_reg), [str(m.indice) for m in v.produto], str(v.prestacoes)] for v in VENDAS]
                save(arquivos["vendas"], DATA_V)

                print("\n 1) Voltar \n 2) Sair do Programa", "\n")
                comando([venda_menu])
            else:
                nov_venda()

        cabeçalho("Menu de Vendas")
        print("\n 1) Nova Venda \n 2) Registo de Vendas \n 3) Voltar \n 4) Sair do Programa", "\n")
        comando([nov_venda, reg_venda, menuprinc])

    def clientes_menu ():

        def reg_clientes ():
            print("\n == Registro de Clientes == \n")
            print(CLIENTES)
            print("\n 1) Voltar \n 2) Sair", "\n")
            comando([clientes_menu])

        def nov_client ():
            print("\n == Novo Cliente == \n")
            nome = str(input(" Nome do Cliente: "))
            identificacao = str(input(" RG ou CPF: "))
            cont = int(input(" Contato: "))
            CLIENTES.append(Cliente(nome, identificacao, cont))
            DATA_C = [[str(c.nome), str(c.id), str(c.contato)] for c in CLIENTES]
            save(arquivos["clientes"], DATA_C)
            print("\n 1) Novo Cliente \n 2) Registo de Clientes \n 3) Voltar \n 4) Sair", "\n")
            comando((nov_client, reg_clientes, menuprinc))

        cabeçalho("Menu de Clientes")
        print(" 1) Novo Cliente \n 2) Registo de Clientes \n 3) Voltar \n 4) Sair", "\n")

        comando((nov_client, reg_clientes, menuprinc))

    def motocicleta_menu ():

        def reg_prod ():
            print("\n == Registro de Motocicletas == \n")
            print(MOTOCICLETAS)
            print("\n 1) Voltar \n 2) Sair", "\n")
            comando([motocicleta_menu])

        def nov_prod ():
            print("\n == Nova Motocicleta == \n")
            while True:
                try:
                    model = str(input(" Modelo: "))
                    ano = int(input(" Ano: "))
                    valor = int(input(" Valor de Fábrica: "))
                    unid = int(input(" Quantidade em Estoque: "))
                except:
                    print("Dados inválidos! \n Tente novamente. \n")
                else:
                    MOTOCICLETAS.append(Motocicleta(model, abs(ano), abs(valor), abs(unid)))
                    DATA_M = [[m.modelo, str(m.ano), str(m.valor), str(m.estoque)] for m in MOTOCICLETAS]
                    save(arquivos["motocicletas"], DATA_M)
                    break

            print("\n 1) Nova Motocicleta \n 2) Registro de Motocicletas \n 3) Voltar \n 4) Sair", "\n")
            comando((nov_prod, reg_prod, motocicleta_menu))

        print('\n =================== \n', "Sistema de Vendas \n", '=================== \n',
              "=== Menu de Motocicletas ===")
        print(" 1) Nova Motocicleta \n 2) Registro de Motocicletas \n 3) Voltar \n 4) Sair", "\n")
        comando((nov_prod, reg_prod, menuprinc))

    cabeçalho("Menu Principal")
    print(" 1) Vendas \n 2) Clientes \n 3) Motocicletas \n 4) Sair do Programa", "\n")
    OPCOES = (venda_menu, clientes_menu, motocicleta_menu)
    comando(OPCOES)


if __name__ == '__main__':
    # try:
    menuprinc()

    # except:
    # print("Programa Encerrado")
