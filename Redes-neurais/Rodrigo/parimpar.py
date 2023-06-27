par =  []
impar = []
todos = []
for i in range (1,21):
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
todos = par + impar
todos.sort()
print(f'VETOR PAR: {par}')
print(f'VETOR IMPAR: {impar}')
print(f'VETOR TODOS:{todos}')