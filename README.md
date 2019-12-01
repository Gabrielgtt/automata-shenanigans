# automata-shenanigans
Implementação de algumas operações com autômatos.\
Todos os códigos foram feito em python3!\
Autômatos devem ser descritos em arquivos conforme o seguinte exemplo:
>estados A, B
>inicial A
>aceita B
>A B 0
>B A 0
>A A 1
>B B 1

### Para checar se uma palavra é aceita por um autômato
`python3 simular.py <arquivo do automato> <palavra>` 
Exemplo:
`python3 simular.py inputs/automato1 101`

### Para converter um AFN para AFD
`python3 simular.py <arquivo automato1> <arquivo automato2>` 
Exemplo:
`python3 simular.py inputs/automato1 inputs/automato2`

