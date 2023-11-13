function partition(array, low, high) {
    let pivot = array[high];
    let init = low - 1;

    for (let currentPosition = low; currentPosition < high; currentPosition++) {
        if (array[currentPosition] <= pivot) {
            init = init + 1;

            [array[init], array[currentPosition]] = [array[currentPosition], array[init]];
        }
    }

    [array[init + 1], array[high]] = [array[high], array[init + 1]];
    return init + 1;
}

function quicksort(array, low, high) {
    if (low < high) {
        let pivot_init = partition(array, low, high);
        quicksort(array, low, pivot_init - 1);
        quicksort(array, pivot_init + 1, high);
    }
}

let array = Array.from({ length: 10 }, () => Math.floor(Math.random() * 100) + 1);

let size = array.length;

quicksort(array, 0, size - 1);
console.log('Array ordenado:', array.join(', '));
