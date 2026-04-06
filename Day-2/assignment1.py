for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i}*{j} = {i*j}')

names = ['Opendra', 'kabiraj', 'Dipak', 'Risan','Sharad']
for key, name in enumerate(names, start=1):
    print(f'{key}.{name}')


for num in range(1, 50):
    if num % 2 == 0:
        print(num)