from modelos import normalizar_referencias, finalizar

def simular_working_set(referencias, quantidade_quadros, tau=4):
    """
    Conjunto de Trabalho: tenta remover paginas cujo ultimo uso ocorreu
    ha pelo menos tau referencias. Se todas forem recentes, remove a mais antiga.
    """
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
                antigas = [p for p in quadros if tempo - ultimo_uso[p] >= tau]
                candidatos = antigas if antigas else quadros
                vitima = min(candidatos, key=lambda p: ultimo_uso[p])
                quadros[quadros.index(vitima)] = pagina
                del ultimo_uso[vitima]
        ultimo_uso[pagina] = tempo
        historico.append((pagina, list(quadros), falta))
    return finalizar("Conjunto de Trabalho", faltas, acertos, historico)

