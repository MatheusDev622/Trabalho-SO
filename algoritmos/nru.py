from modelos import normalizar_referencias, finalizar

def simular_nru(referencias, quantidade_quadros, intervalo_reset=4):
    """
    NRU: classe 0=(R0,M0), 1=(R0,M1), 2=(R1,M0), 3=(R1,M1).
    Os bits R sao zerados a cada intervalo_reset referencias.
    """
    refs = normalizar_referencias(referencias)
    quadros = []
    bits = {}  # pagina: [R, M]
    faltas = acertos = 0
    historico = []

    for tempo, (pagina, escrita) in enumerate(refs, start=1):
        if tempo > 1 and (tempo - 1) % intervalo_reset == 0:
            for estado in bits.values():
                estado[0] = 0

        falta = pagina not in quadros
        if not falta:
            acertos += 1
        else:
            faltas += 1
            if len(quadros) < quantidade_quadros:
                quadros.append(pagina)
            else:
                classe = lambda p: 2 * bits[p][0] + bits[p][1]
                vitima = min(quadros, key=classe)
                quadros[quadros.index(vitima)] = pagina
                del bits[vitima]
            bits[pagina] = [0, 0]

        bits[pagina][0] = 1
        if escrita:
            bits[pagina][1] = 1
        historico.append((pagina, list(quadros), falta))
    return finalizar("NRU", faltas, acertos, historico)

