lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 12,
         'Mochila', 120.50,
         'Canetas', 22,
         'Livros', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>5.2f}')
print('-' * 40)
print(f'{"MATERIAIS PARA INICIAR O ANO LETIVO":^40}')
print('-' * 40)