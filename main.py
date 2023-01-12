import functions
import tracemalloc
import time
import networkx as nx

print("\n\n ------ Bem vindo ao nosso trabalho 2! ------ \n\n")


def main():
    
    functions.limparInicio()

    print("Para começar, digite o caminho para o arquivo do grafo: ")
    path = str(input())

    while (functions.validarArquivo(path) == False):
        print("\n ❌ OPS! Esse arquivo não existe. ❌\n\nPor favor, tente novamente:")
        path = str(input())

    G = functions.lerArquivoGrafos(path)

    prim_linha = functions.primeiralinha(path)
    #print(prim_linha)

    if (functions.gerarArquivoSaida(G) == True):
        print("\n✅ Arquivo de saída salvo com sucesso! ✅\n")
    else:
        print("❌ Erro ao salvar o arquivo de saída! ❌")
        exit()

    
    # Opções de visualização
    print("\nEscolha a forma de visualização que seja utilizar:")
    print("[ 1 ] Matriz de adjacências\n[ 2 ] Lista de adjacências\n[ 3 ] Lista e Matriz de adjacências\n[ 4 ] Nenhuma\n")
    visualizacao = (input("Opção: "))

    while (visualizacao != '1' and visualizacao != '2' and visualizacao != '3' and visualizacao != '4'):
        print("\n ❌ OPS! Essa opção não existe. ❌\n\nPor favor, tente novamente:")
        visualizacao = (input("Opção: "))

    tracemalloc.start()
    ini = time.time()

    if (visualizacao == '1'):
        matriz = functions.criarMatriz(G)
        print("\n✅ Matriz de adjacências salva com sucesso! ✅\n") if matriz == True else print(
            "\n❌ Erro ao salvar a Matriz de adjacências! ❌\n")

    elif (visualizacao == '2'):
        lista = functions.criarLista(G)
        print("\n✅ Lista de adjacências salva com sucesso! ✅\n") if lista == True else print(
            "\n❌ Erro ao salvar a lista de adjacências! ❌\n")

    elif (visualizacao == '3'):
        matriz = functions.criarMatriz(G)
        print("\n✅ Matriz de adjacências salva com sucesso! ✅\n") if matriz != False else print(
            "\n❌ Erro ao salvar a Matriz de adjacências! ❌\n")

        lista = functions.criarLista(G)
        print("✅ Lista de adjacências salva com sucesso! ✅\n") if lista != False else print(
            "\n❌ Erro ao salvar a lista de adjacências! ❌\n")

    fim = time.time()
    print ("Função soma1: ", fim-ini)
    second_size, consumoMem = tracemalloc.get_traced_memory()
    print('Consumo de memória: ', f'{"{:.3f}".format(consumoMem / 10**6)}MB')

    tracemalloc.stop()

    ##
    ##ALGORITMO DE DIJKSTRA
    ##

    if((nx.is_weighted(G) == True) and (functions.verifica_peso(G) == 'Pode usar o algoritmo de Dijkstra') ):
        print("Pode usar o algoritmo de Dijkstra ")
        print("\nDeseja utilizar o algoritmo de Dijkstra?")
        print("[ 1 ] Sim\n[ 2 ] Não\n")
        realizarDijkstra = (input("Opção: "))

        while (realizarDijkstra != '1' and realizarDijkstra!= '2'):
            print("\n ❌ OPS! Essa opção não existe. ❌\n\nPor favor, tente novamente:")
            realizarDijkstra = (input("Opção: "))

        if (realizarDijkstra == '1'):
            #print("\nA partir de qual vértice deseja que seja realizada o algoritmo de Dijkstra?\n")
            vertice_1 = int(1)
            #print("\n Qual o ultimo vértice que deseja analisar com o  algoritmo de Dijkstra?\n")
            vertice_2 = int(10)
            busca = functions.Dijkstra(G , vertice_1 , vertice_2, prim_linha)
            print("\n✅ Caminho com o algoritmo de Dijkstra realizado com sucesso! ✅\n") if busca != False else print("\n❌ Erro ao realizar o algoritmo de Dijkstra  ❌\n")
            #print(busca,"\n",caminho)

    elif( (nx.is_weighted(G) == True) and (functions.verifica_peso(G) == 'Não pode usar o algoritmo de Dijkstra')):
        print("Não pode usar o algoritmo de distancia e caminho de Dijkstra ")

    else:
        # Busca por largura
        print("\nDeseja realizar a busca por largura e profundidade?")
        print("[ 1 ] Sim\n[ 2 ] Não\n")
        realizarBusca = (input("Opção: "))

        while (realizarBusca != '1' and realizarBusca != '2'):
            print("\n ❌ OPS! Essa opção não existe. ❌\n\nPor favor, tente novamente:")
            realizarBusca = (input("Opção: "))

        if (realizarBusca == '1'):
            print("\nA partir de qual vértice deseja que seja realizada a busca por largura e profundidade?\n")
            verticeBusca = (input("Vértice: "))
            busca = functions.buscaLargura(G, verticeBusca)
            print("\n✅ Busca por largura e profundidade salva com sucesso! ✅\n") if busca != False else print(
                "\n❌ Erro ao realizar a busca por largura e profundidade! ❌\n")


        #Descobrir componentes
        print("\nDeseja descobrir os componentes conexos desse grafo?")
        print("[ 1 ] Sim\n[ 2 ] Não\n")
        descobrirComponentes = (input("Opção: "))

        while (descobrirComponentes != '1' and descobrirComponentes != '2'):
            print("\n ❌ OPS! Essa opção não existe. ❌\n\nPor favor, tente novamente:")
            descobrirComponentes = (input("Opção: "))

        if (descobrirComponentes == '1'):
            componentes = functions.buscarComponentes(G)
            print("\n✅ Busca por componentes conexos salva com sucesso! ✅\n") if componentes != False else print(
                "\n❌ Erro ao realizar a busca por componentes conexos! ❌\n")


main()
