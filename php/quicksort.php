<?php

function partition(&$array, $low, $high) {
    $pivot = $array[$high];
    $init = $low - 1;

    for ($currentPosition = $low; $currentPosition < $high; $currentPosition++) {
        if ($array[$currentPosition] <= $pivot) {
            $init = $init + 1;
            list($array[$init], $array[$currentPosition]) = array($array[$currentPosition], $array[$init]);
        }
    }

    list($array[$init + 1], $array[$high]) = array($array[$high], $array[$init + 1]);
    return $init + 1;
}

function quicksort(&$array, $low, $high) {
    if ($low < $high) {
        $pivot_init = partition($array, $low, $high);
        quicksort($array, $low, $pivot_init - 1);
        quicksort($array, $pivot_init + 1, $high);
    }
}

$array = array_map(function() { return mt_rand(1, 100); }, range(1, 10));
$size = count($array);

quicksort($array, 0, $size - 1);
echo 'Array ordenado: ' . implode(', ', $array);
?>
