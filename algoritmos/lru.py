from modelos import normalizar_referencias, finalizar

def simular_lru(referencias, quantidade_quadros):
    refs = normalizar_referencias(referencias)
    quadros = []
    ultimo_uso = {}
    faltas = acertos = 0
    historico = []

    for tempo, (pagina, escrita) in enumerate(refs): #percorre referências
        falta = pagina not in quadros                #verifica se pagina ta na memoria
        if not falta:
            acertos += 1                             #se tiver acerto
        else:
            faltas += 1                              #se nn tiver falta
            if len(quadros) < quantidade_quadros:
                quadros.append(pagina)               #se tiver espaço adiciona pagina
            else:
                vitima = min(quadros, key=lambda p: ultimo_uso[p])
                quadros[quadros.index(vitima)] = pagina        #se tiver cheia, substitui pag mais tempo sem ser acessada
        ultimo_uso[pagina] = tempo
        historico.append((pagina, list(quadros), falta))
    return finalizar("LRU", faltas, acertos, historico)

