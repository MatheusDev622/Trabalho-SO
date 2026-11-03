from algoritmos import (
    simular_otimo, simular_nru, simular_fifo, simular_segunda_chance,
    simular_clock, simular_lru, simular_aging,
    simular_working_set, simular_wsclock,
)

def comparar_algoritmos(referencias, quantidade_quadros, tau=4):
    """Executa todos os algoritmos e imprime uma tabela comparativa."""
    simuladores = [
        simular_otimo,
        simular_nru,
        simular_fifo,
        simular_segunda_chance,
        simular_clock,
        simular_lru,
        simular_aging,
        simular_working_set,
        simular_wsclock,
    ]

    resultados = []
    for simulador in simuladores:
        if simulador in (simular_working_set, simular_wsclock):
            resultado = simulador(referencias, quantidade_quadros, tau=tau)
        else:
            resultado = simulador(referencias, quantidade_quadros)
        resultados.append(resultado)

    total = len(referencias)
    print(f"\nReferencias: {total} | Quadros: {quantidade_quadros}\n")
    print(f"{'Algoritmo':<27} {'Faltas':>8} {'Acertos':>8} {'Taxa de faltas':>16}")
    print("-" * 63)
    for r in sorted(resultados, key=lambda x: x.faltas):
        taxa = (r.faltas / total * 100) if total else 0
        print(f"{r.algoritmo:<27} {r.faltas:>8} {r.acertos:>8} {taxa:>15.1f}%")
    return resultados


def mostrar_historico(resultado):
    """Mostra o estado dos quadros apos cada referencia."""
    print(f"\nHistorico: {resultado.algoritmo}")
    print(f"{'Pagina':>8} {'Quadros':<25} {'Resultado':>12}")
    print("-" * 50)
    for pagina, quadros, falta in resultado.historico:
        estado = "FALTA" if falta else "ACERTO"
        print(f"{pagina:>8} {str(quadros):<25} {estado:>12}")
