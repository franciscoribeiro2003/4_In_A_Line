# Tempos por teste
## Teste 1
```
X
1
4
3
4
4
6
7
6
2
7
1
6
7
2
1
5
5

```
## Minimax
Para alterar a depth ir á função `def get_cpu_move` e alterar o número no primeiro return:
```python
    if difficulty == 1:
        return minimax(board, i_ALTERAR_PARA_UM_NUMERO, NotSymbol)[1]
```


### Depth = 7

```shell
CPU won!
- - - - - - - 
- - - X - - - 
- - - O - - - 
- - - X - X - 
- - - O O O O 
O - X X O X X 
1 2 3 4 5 6 7



real	2m50,344s
user	2m50,826s
sys	0m1,116s
```

### Depth = 6
```shell
You won!
- X - - - O X 
- O - O - X X 
X O - X - X O 
O O - X X O O 
O X - O O X O 
X O X X X O X 
1 2 3 4 5 6 7



real	0m40,922s
user	0m40,925s
sys	0m0,641s
```

### Depth = 5
```shell
CPU won!
- - - - - - - 
- - - - - - - 
- - - X O - - 
- - - X O X O 
- - - O O O X 
- X X X O X O 
1 2 3 4 5 6 7



real	0m4,832s
user	0m4,780s
sys	0m0,516s
```

### Depth = 4
```shell
CPU won!
- O - O - X X 
- O - O O O O 
- X - X X X O 
- O - X O O X 
X X - O X X O 
X O X X O O X 
1 2 3 4 5 6 7



real	0m1,491s
user	0m1,423s
sys	0m0,513s
```

### Depth = 4
```shell
CPU won!
- - - - - - - 
- - - - - - - 
- - - X - - - 
- - - X - - - 
- - O O O O - 
- - X X O X - 
1 2 3 4 5 6 7



real	0m0,549s
user	0m0,436s
sys	0m0,549s
```
