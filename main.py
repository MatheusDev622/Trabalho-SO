from comparacao import comparar_algoritmos, mostrar_historico

if __name__ == "__main__":
    # Altere a sequencia e a quantidade de quadros para testar outros casos.
    referencias = [1, 2, 3, 1, 4, 2, 5, 1, 2, 3, 4, 5]
    quantidade_quadros = 3

    resultados = comparar_algoritmos(
        referencias,
        quantidade_quadros,
        tau=4
    )

    # Mostra o passo a passo do LRU.
    resultado_lru = next(r for r in resultados if r.algoritmo == "LRU")
    mostrar_historico(resultado_lru)
