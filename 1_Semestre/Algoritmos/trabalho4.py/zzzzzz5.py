n = int(input('O fatorial de: '))

fat = 1
for c in range(1,n+1):
    fat *= c
print('O fatorial é',fat)