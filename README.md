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
