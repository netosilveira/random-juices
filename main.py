import random

flavs = ['spear might', 'cola', 'g pnpl', 'sweet mango', 'pineapple', 'ws', 'd watermelon', 'uva', 'pnpl inw']
sort = random.randint(0,len(flavs))

print('sabores disponiveis: ')

for i in flavs:
    print(' -', i)

for i in range(2):
    print(flavs[sort])