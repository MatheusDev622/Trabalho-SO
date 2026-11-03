from modelos import normalizar_referencias, finalizar

def simular_segunda_chance(referencias, quantidade_quadros):
    refs = normalizar_referencias(referencias)
    quadros = []
    bit_r = {}
    fila = []
    faltas = acertos = 0
    historico = []

    for pagina, escrita in refs:
        falta = pagina not in quadros
        if not falta:
            acertos += 1
            bit_r[pagina] = 1
        else:
            faltas += 1
            if len(quadros) < quantidade_quadros:
                quadros.append(pagina)
            else:
                while True:
                    candidata = fila.pop(0)
                    if bit_r[candidata] == 0:
                        quadros[quadros.index(candidata)] = pagina
                        del bit_r[candidata]
                        break
                    bit_r[candidata] = 0
                    fila.append(candidata)
            fila.append(pagina)
            bit_r[pagina] = 1
        historico.append((pagina, list(quadros), falta))
    return finalizar("Segunda Chance", faltas, acertos, historico)

