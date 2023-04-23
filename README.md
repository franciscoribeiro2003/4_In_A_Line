# 4_In_A_Line
4 em linha



## ConnectFour.py 

**requisitos**
- install `pygame` com `pip install pygame`

### Alterar profundidades
Para alterar a depth ir á função `def get_cpu_move` e alterar o número no primeiro return:

- **Minimax**  Aguenta com 6 mas resposta tardia
```python
    if difficulty == 1:
        return minimax(board, i_ALTERAR_PARA_UM_NUMERO, NotSymbol)[1]
```

- **Alphabeta**  Aguenta com 8 mas resposta tardia
```python
    if difficulty == 2:
        return alphabeta(board, i_ALTERAR_PARA_UM_NUMERO, NotSymbol, alpha, beta)[1]
```




