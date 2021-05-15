n = int(input("Insira o valor de meses: "))
k = int(input("Insira o valor de pares por geracao: "))

Fn = [1, 1]
Fn.append(1+k) #F3 sempre é 1 + o numero K de pares

for i in range(3, n):
    A = Fn[i-2] * k + Fn[i-1] 
    Fn.append(A)

print(Fn[n-1])