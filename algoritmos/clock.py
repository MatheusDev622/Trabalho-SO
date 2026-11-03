from modelos import normalizar_referencias, finalizar

def simular_clock(referencias, quantidade_quadros):
    refs = normalizar_referencias(referencias)
    quadros = [None] * quantidade_quadros
    bit_r = [0] * quantidade_quadros
    ponteiro = 0
    faltas = acertos = 0
    historico = []

    for pagina, escrita in refs:
        if pagina in quadros:
            acertos += 1
            bit_r[quadros.index(pagina)] = 1
            falta = False
        else:
            faltas += 1
            falta = True
            while quadros[ponteiro] is not None and bit_r[ponteiro] == 1:
                bit_r[ponteiro] = 0
                ponteiro = (ponteiro + 1) % quantidade_quadros
            quadros[ponteiro] = pagina
            bit_r[ponteiro] = 1
            ponteiro = (ponteiro + 1) % quantidade_quadros
        historico.append((pagina, [p for p in quadros], falta))
    return finalizar("Relogio (Clock)", faltas, acertos, historico)

