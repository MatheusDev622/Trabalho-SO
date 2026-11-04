from comparacao import comparar_algoritmos, mostrar_historico

if __name__ == "__main__":
    referencias = [
        2, 1, 5, 4, 4, 3, 2, 9, 2, 10,
        7, 1, 1, 2, 4, 4, 9, 10, 1, 9,
        4, 9, 7, 4, 8, 10, 5, 1, 3, 7,
        6, 5, 3, 4, 6, 2, 2, 7, 2, 6,
        6, 5, 1, 8, 9, 2, 7, 2, 9, 5,
        10, 6, 10, 4, 2, 1, 4, 5, 2, 4,
        2, 7, 5, 8, 6, 3, 6, 6, 4, 5,
        2, 10, 3, 9, 4, 3, 8, 7, 5, 9,
        4, 6, 1, 4, 10, 2, 2, 9, 7, 2,
        10, 5, 6, 4, 2, 4, 2, 7, 10, 5
        ]
        
    quantidade_quadros = 4

    resultados = comparar_algoritmos(
        referencias,
        quantidade_quadros,
        tau=4
    )

    # Mostra o passo a passo do LRU.
    resultado_lru = next(r for r in resultados if r.algoritmo == "LRU")
    mostrar_historico(resultado_lru)
