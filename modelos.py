from dataclasses import dataclass

@dataclass
class Resultado:
    algoritmo: str
    faltas: int
    acertos: int
    historico: list

def normalizar_referencias(referencias):
    """Converte referencias para pares (pagina, escrita)."""
    resultado = []
    for item in referencias:
        if isinstance(item, tuple):
            pagina, escrita = item
            resultado.append((pagina, bool(escrita)))
        else:
            resultado.append((item, False))
    return resultado


def finalizar(nome, faltas, acertos, historico):
    return Resultado(nome, faltas, acertos, historico)

