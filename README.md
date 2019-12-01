# automata-shenanigans
Implementação de algumas operações com autômatos.\
Todos os códigos foram feito em python3!\
Autômatos devem ser descritos em arquivos conforme o seguinte exemplo:
>estados A, B\
>inicial A\
>aceita B\
>A B 0\
>B A 0\
>A A 1\
>B B 1

### Para checar se uma palavra é aceita por um autômato
Comando:\
`python3 simular.py <arquivo do automato> <palavra>`\
Exemplo:\
`python3 simular.py inputs/automato1 101`

### Para converter um AFN para AFD
Comando:\
`python3 converte_AFN.py <arquivo automato>`\
Exemplo:\
`python3 converte_AFN.py inputs/automato1`

### Para obter o complemento de um autômato
Comando:\
`python3 complemento_automato.py <arquivo automato>`\
Exemplo:\
`python3 complemento_automato.py inputs/automato1`

### Para obter a união entre dois autômatos
Comando:\
`python3 uniao_automatos.py <arquivo automato1> <arquivo automato2>`\
Exemplo:\
`python3 uniao_automatos.py inputs/automato1 inputs/automato2`
