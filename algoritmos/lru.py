from modelos import normalizar_referencias, finalizar

def simular_lru(referencias, quantidade_quadros):
    refs = normalizar_referencias(referencias)
    quadros = []
    ultimo_uso = {}
    faltas = acertos = 0
    historico = []

    for tempo, (pagina, escrita) in enumerate(refs):
        falta = pagina not in quadros
        if not falta:
            acertos += 1
        else:
            faltas += 1
            if len(quadros) < quantidade_quadros:
                quadros.append(pagina)
            else:
                vitima = min(quadros, key=lambda p: ultimo_uso[p])
                quadros[quadros.index(vitima)] = pagina
        ultimo_uso[pagina] = tempo
        historico.append((pagina, list(quadros), falta))
    return finalizar("LRU", faltas, acertos, historico)

