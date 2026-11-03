from modelos import normalizar_referencias, finalizar

def simular_wsclock(referencias, quantidade_quadros, tau=4):
    """
    WSClock simplificado: percorre os quadros circularmente.
    Paginas referenciadas recentemente recebem segunda chance (R=0).
    Paginas antigas e limpas sao substituidas; paginas antigas e modificadas
    sao consideradas gravadas e podem ser substituidas nessa mesma passagem.
    """
    refs = normalizar_referencias(referencias)
    quadros = [None] * quantidade_quadros
    bit_r = [0] * quantidade_quadros
    bit_m = [0] * quantidade_quadros
    ultimo_uso = [0] * quantidade_quadros
    ponteiro = 0
    faltas = acertos = 0
    historico = []

    for tempo, (pagina, escrita) in enumerate(refs, start=1):
        if pagina in quadros:
            acertos += 1
            idx = quadros.index(pagina)
            bit_r[idx] = 1
            ultimo_uso[idx] = tempo
            if escrita:
                bit_m[idx] = 1
            falta = False
        else:
            faltas += 1
            falta = True
            # Primeiro procura quadro vazio.
            vazios = [i for i, p in enumerate(quadros) if p is None]
            if vazios:
                idx = vazios[0]
            else:
                idx = None
                for _ in range(2 * quantidade_quadros):
                    i = ponteiro
                    idade = tempo - ultimo_uso[i]
                    if bit_r[i] == 1:
                        bit_r[i] = 0
                    elif idade >= tau and bit_m[i] == 0:
                        idx = i
                        break
                    elif idade >= tau and bit_m[i] == 1:
                        # Simula a escrita da pagina modificada em disco.
                        bit_m[i] = 0
                    ponteiro = (ponteiro + 1) % quantidade_quadros

                if idx is None:
                    # Fallback: substitui a pagina menos recentemente usada.
                    idx = min(range(quantidade_quadros), key=lambda i: ultimo_uso[i])

            quadros[idx] = pagina
            bit_r[idx] = 1
            bit_m[idx] = int(escrita)
            ultimo_uso[idx] = tempo
            ponteiro = (idx + 1) % quantidade_quadros

        historico.append((pagina, list(quadros), falta))
    return finalizar("WSClock", faltas, acertos, historico)

