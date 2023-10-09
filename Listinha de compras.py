total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Produto:  '))
    preço = float(input('Preço: R$  '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Algo mais: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA!'))
print(f'O total foi de R$ {total:.2f}.')
print(f'Foram {totmil} produtos acima de R$1000.')
print(f'O produto mais barato foi o {barato} que custa R$ {menor:.2f}.')