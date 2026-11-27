from modelos import normalizar_referencias, finalizar

def simular_aging(referencias, quantidade_quadros, bits_contador=8):
    """Aging: desloca os contadores e insere o bit R no bit mais significativo."""
    refs = normalizar_referencias(referencias)
    quadros = []
    contador = {}
    bit_r = {}
    faltas = acertos = 0
    historico = []
    mascara = (1 << bits_contador) - 1
    bit_alto = 1 << (bits_contador - 1)

    for pagina, escrita in refs:
        # Atualizacao periodica simplificada: uma vez por referencia.
        for p in list(quadros):
            contador[p] = (contador[p] >> 1) & mascara    #desloca contador pra direita, tirando importancia dos valores antigos
            if bit_r[p]:
                contador[p] |= bit_alto     #se pagina usada, coloca 1 no bit mais significativo
            bit_r[p] = 0                    #zer bit pra prox contagem

        falta = pagina not in quadros
        if not falta:
            acertos += 1
        else:
            faltas += 1
            if len(quadros) < quantidade_quadros:
                quadros.append(pagina)
            else:
                vitima = min(quadros, key=lambda p: contador[p])
                quadros[quadros.index(vitima)] = pagina
                del contador[vitima]                  #se tiver cheia adiciona menor contador pra ser removido
                del bit_r[vitima]
            contador[pagina] = 0
            bit_r[pagina] = 0
        bit_r[pagina] = 1                                       #pag utilizada
        historico.append((pagina, list(quadros), falta))
    return finalizar("Envelhecimento (Aging)", faltas, acertos, historico)

