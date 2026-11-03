from modelos import normalizar_referencias, finalizar

def simular_otimo(referencias, quantidade_quadros):
    refs = normalizar_referencias(referencias)
    paginas = [p for p, _ in refs]
    quadros = []
    faltas = acertos = 0
    historico = []

    for i, (pagina, escrita) in enumerate(refs):
        falta = pagina not in quadros
        if not falta:
            acertos += 1
        else:
            faltas += 1
            if len(quadros) < quantidade_quadros:
                quadros.append(pagina)
            else:
                proximo_uso = {}
                for p in quadros:
                    try:
                        proximo_uso[p] = paginas.index(p, i + 1)
                    except ValueError:
                        proximo_uso[p] = float("inf")
                vitima = max(quadros, key=lambda p: proximo_uso[p])
                quadros[quadros.index(vitima)] = pagina
        historico.append((pagina, list(quadros), falta))
    return finalizar("Otimo (teorico)", faltas, acertos, historico)

