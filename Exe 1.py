#1. Faça um programa que leia um vetor de 5

vetor = []
print("Informe os 5 numeros")
for i in range(5):
    vetor.append(input("numero" + str(i+1) + ":\n"))
print(vetor)