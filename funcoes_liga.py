import random

###############################################################################
#                               Liga - xAyBzC                                 #
###############################################################################


def gene_peso(valor_max):
    """Sorteia 3 valores x,y,z tal que x + y + z = valor máximo.
    
    Args:
      valor_max: Informa o valor de massa total."""

    x = random.choice(list(range(5,91)))
    y = random.choice(list(range(5,96-x)))
    z = 100 - x- y

    gene = [x, y, z]

    return gene

def gene_elementos(valores_possiveis):
    """ Sorteia três elementos para compor a liga.
    
    valores_possiveis: informa todos os elementos possíveis."""

    gene = random.sample(valores_possiveis, 3)

    return gene


def cria_candidato_liga(valores_possiveis, valor_max):
    """Cria uma lista com 3 valores de elementos seguidos de 3 valores de seus pesos respectivos.

    Args:
      velores_possiveis: lista de elementos a serem sorteados.
      valor_max: inteiro represtando o valor máximo do peso total da liga.
    """
    elementos = gene_elementos(valores_possiveis)
    pesos = gene_peso(valor_max)

    candidato = elementos + pesos

    return candidato 


def populacao_ligas(tamanho, valores_possiveis, valor_max):
    """Cria uma população para o problema das ligas ternárias.

    Args:
      tamanho: tamanho da população
      velores_possiveis: lista de elementos a serem sorteados.
      valor_max: inteiro represtando o valor máximo ddo peso total da liga.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(cria_candidato_liga(valores_possiveis, valor_max))
    return populacao


def funcao_objetivo_liga(candidato, dic_peso_atomico, dic_preco):
    """Computa a função objetivo no problema de ligas ternárias.

    Args:
      candidato: uma lista contendo os três primeiros valores sendo elementos,
      e os últimos três seus pesos atômicos
    """
    peso_molecular = 0
    valor_liga = 0

    for elemento, massa in zip(candidato, candidato[3:]):
        peso_elemento = dic_peso_atomico[elemento]
        peso_molecular += peso_elemento*massa

        valor_liga += dic_preco[elemento]*massa

    peso_molecular /= 100
    valor_liga /= 1000

    return valor_liga - peso_molecular


def funcao_objetivo_pop_liga(populacao, dic_peso_atomico, dic_preco):
    """Computa a função objetivo para uma população no problema de ligas ternárias.

    Args:
      populacao: lista contendo os individuos do problema.

    """
    fitness = []
    for individuo in populacao:
        fitness.append(funcao_objetivo_liga(individuo, dic_peso_atomico, dic_preco))
    return fitness


def selecao_torneio_max(populacao, fitness, tamanho_torneio):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    maximização.

    Args:
      populacao: lista contendo os individuos do problema
      fitness: lista contendo os valores computados da funcao objetivo
      tamanho_torneio: quantidade de invíduos que batalham entre si

    """
    selecionados = []

    for _ in range(len(populacao)):
        sorteados = random.sample(populacao, tamanho_torneio)

        fitness_sorteados = []
        for individuo in sorteados:
            indice_individuo = populacao.index(individuo)
            fitness_sorteados.append(fitness[indice_individuo])

        max_fitness = max(fitness_sorteados)
        indice_max_fitness = fitness_sorteados.index(max_fitness)
        individuo_selecionado = sorteados[indice_max_fitness]

        selecionados.append(individuo_selecionado)

    return selecionados
    

def cruzamento_ordenado_liga(pai, mae, chance_de_cruzamento):
    """Cruzamento ordenado entre dois individuos.

    Args:
      pai: lista representando um individuo.
      mae: lista representando um individuo.
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento.

    """
    pai, pai_pesos = pai[:3], pai[3:]
    mae, mae_pesos = mae[:3], mae[3:]
    
    if random.random() < chance_de_cruzamento:
        tamanho_individuo = len(mae[:3])

        # pontos de corte
        corte1 = random.randint(0, tamanho_individuo - 2)
        corte2 = random.randint(corte1 + 1, tamanho_individuo)

        # filho1
        filho1 = [None] * tamanho_individuo
        filho1[corte1:corte2] = mae[corte1:corte2]
        pai_ = pai[corte2:] + pai[:corte2]
        posicao = corte2 % tamanho_individuo
        for valor in pai_:
            if valor not in filho1:
                filho1[posicao] = valor
                posicao += 1
                posicao %= tamanho_individuo

        # filho2
        filho2 = [None] * tamanho_individuo
        filho2[corte1:corte2] = pai[corte1:corte2]
        mae_ = mae[corte2:] + mae[:corte2]
        posicao = corte2 % tamanho_individuo
        for valor in mae_:
            if valor not in filho2:
                filho2[posicao] = valor
                posicao += 1
                posicao %= tamanho_individuo

        return filho1 + pai_pesos, filho2 + mae_pesos
    else:
        return pai + pai_pesos, mae + mae_pesos
    
def mutacao_peso_liga(populacao, valor_peso, chance_de_mutacao):
    """Realiza mutação simples no problema das ligas ternárias.

    Args:
      populacao: lista contendo os indivíduos do problema.
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação.

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            peso_fixo = random.choice(individuo[3:])
            peso1 = random.choice(list(range(5,96-peso_fixo)))
            peso2 = valor_peso - peso_fixo - peso1

            individuo[3] = peso_fixo
            individuo[4] = peso1
            individuo[5] = peso2


def mutacao_gene_liga(populacao, chance_de_mutacao, valores_possiveis):
    """Realiza mutação de um gene do indivíduo.

    Args:
      populacao: lista contendo os indivíduos do problema.
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação.
      valores_possiveis: lista com todos os valores possíveis dos genes.
    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
          gene = random.randint(0, len(individuo[:3]) - 1)
          valores = valores_possiveis.copy()
          valores.remove(individuo[0])
          valores.remove(individuo[1])
          valores.remove(individuo[2])
          individuo[gene] = random.choice(valores)
