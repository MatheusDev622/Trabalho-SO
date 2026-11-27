"""
Teste com muitas referencias (padrao: 400) geradas aleatoriamente com SEMENTE FIXA.

Como a semente e fixa, qualquer pessoa que rodar o mesmo comando obtem
exatamente a mesma sequencia e os mesmos resultados.

Exemplos:
    python teste_grande.py                          # semente 42, 400 referencias
    python teste_grande.py --semente 7              # outra semente (outra sequencia)
    python teste_grande.py --modo localidade        # acessos com localidade de referencia
    python teste_grande.py --tabelas                # tambem imprime todas as tabelas no terminal

As tabelas passo a passo de todos os algoritmos sao sempre salvas em um .txt
(para nao poluir o terminal com milhares de linhas).
"""
import argparse
import contextlib

from comparacao import (
    comparar_algoritmos,
    comparar_varios_quadros,
    gerar_referencias_aleatorias,
    mostrar_todos_historicos,
)


def main():
    parser = argparse.ArgumentParser(description="Teste grande de substituicao de paginas")
    parser.add_argument("--semente", type=int, default=42, help="semente do gerador (padrao: 42)")
    parser.add_argument("--n", type=int, default=400, help="quantidade de referencias (padrao: 400)")
    parser.add_argument("--paginas", type=int, default=20, help="paginas distintas, de 1 a N (padrao: 20)")
    parser.add_argument("--quadros", type=int, default=5, help="quadros no teste detalhado (padrao: 5)")
    parser.add_argument("--tau", type=int, default=10, help="janela tau do Working Set/WSClock (padrao: 10)")
    parser.add_argument("--modo", choices=["uniforme", "localidade"], default="uniforme")
    parser.add_argument("--tabelas", action="store_true", help="imprime as tabelas passo a passo no terminal")
    parser.add_argument("--arquivo", default=None, help="arquivo de saida das tabelas")
    args = parser.parse_args()

    referencias = gerar_referencias_aleatorias(
        args.n, args.paginas, args.semente, modo=args.modo
    )

    print("=" * 63)
    print("TESTE GRANDE")
    print(f"Semente: {args.semente} | Modo: {args.modo} | Referencias: {args.n}")
    print(f"Paginas distintas: 1..{args.paginas} | tau: {args.tau}")
    print("=" * 63)
    print("Primeiras 20 referencias (pagina, escrita):")
    print(referencias[:20])

    # 1) Comparacao detalhada com uma quantidade de quadros.
    resultados = comparar_algoritmos(referencias, args.quadros, tau=args.tau)

    # 2) Comparacao variando a quantidade de quadros.
    comparar_varios_quadros(referencias, [3, 4, 5, 6, 8, 10], tau=args.tau)

    # 3) Verificacao: o Otimo nunca pode ter mais faltas que os demais.
    otimo = next(r for r in resultados if r.algoritmo.startswith("Otimo"))
    assert all(otimo.faltas <= r.faltas for r in resultados), "Otimo deveria ser o menor!"
    print("\n[OK] Verificacao: o algoritmo Otimo teve o menor numero de faltas.")

    # 4) Tabelas passo a passo de todos os algoritmos.
    arquivo = args.arquivo or f"saida_teste_grande_semente{args.semente}.txt"
    with open(arquivo, "w", encoding="utf-8") as f:
        with contextlib.redirect_stdout(f):
            print(f"Semente: {args.semente} | Modo: {args.modo} | "
                  f"Referencias: {args.n} | Quadros: {args.quadros}")
            mostrar_todos_historicos(resultados)
    print(f"[OK] Tabelas passo a passo de todos os algoritmos salvas em: {arquivo}")

    if args.tabelas:
        mostrar_todos_historicos(resultados)


if __name__ == "__main__":
    main()
