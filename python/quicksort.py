from random import randint


def partition(array, low, high):
	"""
	Função responsável por escolher um elemento como pivô e rearranjar os elementos do array.
	Os elementos menores que o pivô estarão à esquerda e os elementos maiores à direita.
    """
	
	pivot = array[high]
	init = low - 1

	for i in range(low, high):
		if array[i] <= pivot:

			init = init + 1
			
			(array[init], array[i]) = (array[i], array[init])

	(array[init + 1], array[high]) = (array[high], array[init + 1])
	return init + 1


def quicksort(array, low, high):
    """
	Função principal. 
	Recebe uma lista, um índice baixo (low) e um índice alto (high).
	O algoritmo continua dividindo o array até que low < high não seja mais satisfeita.
    """
	
    if low < high:
		
        pivot_init = partition(array, low, high)
        quicksort(array, low, pivot_init - 1)
        quicksort(array, pivot_init + 1, high)
        

array = [randint(1, 100) for i in range(10)]
size = len(array)

quicksort(array, 0, size - 1)
print(f'Array ordenado: {array}')
