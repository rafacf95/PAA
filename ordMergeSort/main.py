def mergeSort(vetor):
    if len(vetor) > 1:
        meio = len(vetor) // 2 # encontra o meio do vetor
        e = vetor[:meio] # separa a metade esquerda do vetor em um novo vetor
        d = vetor[meio:] # separa a metade direita do vetor em um novo vetor
        # chamadas recursiva da função mergeSort para criar vetores auxiliares
        mergeSort(e)
        mergeSort(d)
        # contadores pra percorrer os vetores
        i = j = k = 0

        # verifica em qual vetor auxiliar está o menor valor e o coloca no vetor principal
        while i < len(e) and j < len(d):
            if e[i] < d[j]:
                vetor[k] = e[i]
                i += 1
            else:
                vetor[k] = d[j]
                j += 1
            k += 1

        # verifica se não sobrou nenhum valor nos vetores auxiliares
        while i < len(e):
            vetor[k] = e[i]
            i += 1
            k += 1

        while j < len(d):
            vetor[k] = d[j]
            j += 1
            k += 1

# função para imprimir os valores do vetor
def imprimeVetor(vetor):
    for i in range(len(vetor)):
        print(vetor[i], end = " ")
    print()


vet = [9, 10, -1, 3, 6, 2, 1, -3, 1, 0, -2, 15, 8, -7, 0]
print("Vetor a ser ordenado: ")
imprimeVetor(vet)
mergeSort(vet)
print("Vetor ordenado: ")
imprimeVetor(vet)