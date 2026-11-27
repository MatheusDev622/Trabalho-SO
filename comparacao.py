import random

from algoritmos import (
    simular_otimo, simular_nru, simular_fifo, simular_segunda_chance,
    simular_clock, simular_lru, simular_aging,
    simular_working_set, simular_wsclock,
)

SIMULADORES = [
    simular_otimo,
    simular_nru,
    simular_fifo,
    simular_segunda_chance,
    simular_clock,
    simular_lru,
    simular_aging,
    simular_working_set,
    simular_wsclock,
]


def executar_todos(referencias, quantidade_quadros, tau=4):
    """Executa todos os algoritmos e devolve a lista de Resultado (sem imprimir)."""
    resultados = []
    for simulador in SIMULADORES:
        if simulador in (simular_working_set, simular_wsclock):
            resultado = simulador(referencias, quantidade_quadros, tau=tau)
        else:
            resultado = simulador(referencias, quantidade_quadros)
        resultados.append(resultado)
    return resultados


def comparar_algoritmos(referencias, quantidade_quadros, tau=4):
    """Executa todos os algoritmos e imprime uma tabela comparativa."""
    resultados = executar_todos(referencias, quantidade_quadros, tau)

    total = len(referencias)
    print(f"\nReferencias: {total} | Quadros: {quantidade_quadros}\n")
    print(f"{'Algoritmo':<27} {'Faltas':>8} {'Acertos':>8} {'Taxa de faltas':>16}")
    print("-" * 63)
    for r in sorted(resultados, key=lambda x: x.faltas):
        taxa = (r.faltas / total * 100) if total else 0
        print(f"{r.algoritmo:<27} {r.faltas:>8} {r.acertos:>8} {taxa:>15.1f}%")
    return resultados


def mostrar_historico(resultado):
    """Mostra o estado dos quadros apos cada referencia."""
    print(f"\nHistorico: {resultado.algoritmo}")
    print(f"{'Pagina':>8} {'Quadros':<25} {'Resultado':>12}")
    print("-" * 50)
    for pagina, quadros, falta in resultado.historico:
        estado = "FALTA" if falta else "ACERTO"
        print(f"{pagina:>8} {str(quadros):<25} {estado:>12}")


def mostrar_todos_historicos(resultados):
    """Mostra a tabela passo a passo de TODOS os algoritmos (mesmo formato do LRU)."""
    for resultado in resultados:
        mostrar_historico(resultado)


def gerar_referencias_aleatorias(quantidade, num_paginas, semente,
                                 prob_escrita=0.3, modo="uniforme"):
    """
    Gera uma sequencia de referencias (pagina, escrita) de forma reproduzivel.

    - A mesma semente sempre gera exatamente a mesma sequencia.
    - modo "uniforme": toda pagina de 1..num_paginas tem a mesma chance.
    - modo "localidade": a maior parte dos acessos fica em uma janela de
      paginas que muda de tempos em tempos (simula localidade de referencia).
    """
    rng = random.Random(semente)  # gerador proprio: nao mexe no random global
    referencias = []

    janela = max(3, num_paginas // 4)
    fase = 40
    base = 1

    for i in range(quantidade):
        if modo == "localidade":
            if i % fase == 0:
                base = rng.randrange(1, num_paginas - janela + 2)
            if rng.random() < 0.9:
                pagina = base + rng.randrange(janela)
            else:
                pagina = rng.randrange(1, num_paginas + 1)
        else:
            pagina = rng.randrange(1, num_paginas + 1)

        escrita = rng.random() < prob_escrita
        referencias.append((pagina, escrita))
    return referencias


def comparar_varios_quadros(referencias, lista_quadros, tau=4):
    """
    Imprime uma matriz: linhas = algoritmos, colunas = quantidade de quadros,
    valores = total de faltas de pagina. Devolve {quadros: [Resultado, ...]}.
    """
    por_quadros = {q: executar_todos(referencias, q, tau) for q in lista_quadros}
    total = len(referencias)

    print(f"\nFaltas de pagina por quantidade de quadros ({total} referencias)\n")
    cabecalho = f"{'Algoritmo':<27}" + "".join(f"{q:>8}" for q in lista_quadros)
    print(cabecalho)
    print("-" * len(cabecalho))

    nomes = [r.algoritmo for r in por_quadros[lista_quadros[0]]]
    for i, nome in enumerate(nomes):
        linha = f"{nome:<27}"
        for q in lista_quadros:
            linha += f"{por_quadros[q][i].faltas:>8}"
        print(linha)

    print("\nTaxa de faltas (%)\n")
    print(cabecalho)
    print("-" * len(cabecalho))
    for i, nome in enumerate(nomes):
        linha = f"{nome:<27}"
        for q in lista_quadros:
            linha += f"{por_quadros[q][i].faltas / total * 100:>7.1f}%"
        print(linha)
    return por_quadros

