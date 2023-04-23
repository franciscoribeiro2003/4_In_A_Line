# Connect Four
Autores: Francisco Ribeiro, Matheus Bissacot, Sérgio Coelho
- [Link do Repositorio](https://github.com/franciscoribeiro2003/4_In_A_Line)
## Requisitos
Para ser possıvel correr o programa  ́e necessario ter python instalado assim como a biblioteca pygame.
- Python preferencialmente Python3.
- Pygame Version: 2.3.0

Para instalar Ubuntu/Debian correr o seguinte comando:
```shell
$ sudo apt-get install python3-pygame
```

## Execucao
Para executar o programa, basta correr o seguinte comando:
```shell
$ python python3 ConnectFour.py
```

Abrira uma janela pygame, e pode interagir com ela através da keystrokes no terminal.


Iniciar o Jogo no terminal
```
Welcome to Connect 4!
Good luck!

Choose X(RED, start first) or O(BLACK): X
Choose the algorithm you want to play against:
1: Minimax | 2: Alpha Beta | 3: MCTS
2

- - - - - - - 
- - - - - - - 
- - - - - - - 
- - - - - - - 
- - - - - - - 
- - - - - - - 
1 2 3 4 5 6 7


Make a move by choosing your column (1 to 7): 

```

Pode optar por intruduzir um teste de um documento .txt, para isso correr o seguinte comando:
```shell
$ python python3 ConnectFour.py<teste.txt
```

## Personalizacao
Para personalizar a depht dos algoritmos minimax e alpha beta, basta alterar a variavel DEPTH no ficheiro ConnectFour.py
```python
# Define depth
DEPTH = 5
```

