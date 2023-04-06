# 4_In_A_Line
4 em linha

## p4.py
**Verificar ficheiro time.md com um teste do minimax**


## p5.py **Ficheiro mais recente**
"funciona minimax e alphabeta", em algumas configurações é duvidoso pois prefere defender quando tem 3 do que fazer a jogada final que faz com que ele ganhe 

### alterar profundidades
Para alterar a depth ir á função `def get_cpu_move` e alterar o número no primeiro return:

- **Minimax**  Aguenta com 6 mas resposta tardia
```python
    if difficulty == 1:
        return minimax(board, i_ALTERAR_PARA_UM_NUMERO, NotSymbol)[1]
```

- **Alphabeta**  Aguenta com 8 mas resposta tardia
```python
    if difficulty == 2:
        return minimax(board, i_ALTERAR_PARA_UM_NUMERO, NotSymbol, alpha, beta)[1]
```


**requisitos**
- install `pygame` com `pip install pygame`

