# Simulador de substituicao de paginas

## Estrutura

- `main.py`: ponto de entrada do programa.
- `modelos.py`: estrutura Resultado e funcoes compartilhadas.
- `comparacao.py`: executa e compara todos os algoritmos.
- `algoritmos/`: implementacao individual de cada algoritmo:
  - `fifo.py`
  - `otimo.py`
  - `nru.py`
  - `segunda_chance.py`
  - `clock.py`
  - `lru.py`
  - `envelhecimento.py`
  - `conjunto_trabalho.py`
  - `wsclock.py`

## Como executar

Abra o terminal na pasta do projeto e execute:

    python main.py

Nao e necessario instalar bibliotecas externas.

`main.py` mostra a comparacao e a tabela passo a passo de TODOS os algoritmos.

## Teste grande (mais de 300 referencias, com semente)

    python teste_grande.py

Gera 400 referencias aleatorias com semente fixa (padrao 42): a mesma semente
produz sempre a mesma sequencia e os mesmos resultados. Opcoes:

    python teste_grande.py --semente 7            # outra sequencia
    python teste_grande.py --n 1000               # mais referencias
    python teste_grande.py --modo localidade      # acessos com localidade
    python teste_grande.py --paginas 30 --quadros 6 --tau 10
    python teste_grande.py --tabelas              # imprime tabelas no terminal

As tabelas passo a passo de todos os algoritmos sao salvas em
`saida_teste_grande_semente<N>.txt`.

## Como testar um algoritmo individual

Por exemplo:

    from algoritmos.fifo import simular_fifo

    resultado = simular_fifo([1, 2, 3, 1, 4, 2], 3)
    print("Faltas:", resultado.faltas)
    print("Acertos:", resultado.acertos)

## Formato das referencias

Um numero representa leitura, por exemplo `3`.
Uma tupla representa pagina e escrita, por exemplo `(3, True)`.

Os algoritmos NRU e WSClock usam esses bits de modificacao.
O Aging, Conjunto de Trabalho e WSClock sao modelos simplificados
para fins didaticos; os detalhes estao documentados em seus arquivos.
