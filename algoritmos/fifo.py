from modelos import normalizar_referencias, finalizar

def simular_fifo(referencias, quantidade_quadros):
    refs = normalizar_referencias(referencias)
    quadros = []
    fila = []
    faltas = acertos = 0
    historico = []

    for pagina, escrita in refs:
        falta = pagina not in quadros
        if not falta:
            acertos += 1
        else:
            faltas += 1
            if len(quadros) < quantidade_quadros:
                quadros.append(pagina)
            else:
                vitima = fila.pop(0)
                quadros[quadros.index(vitima)] = pagina
            fila.append(pagina)
        historico.append((pagina, list(quadros), falta))
    return finalizar("FIFO", faltas, acertos, historico)

