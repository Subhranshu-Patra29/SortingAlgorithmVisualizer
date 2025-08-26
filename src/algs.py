from algorithms import *
from algorithms import beadSort, circle_sort, double_sort, intro_sort, iterative_merge_sort, merge_insertion_sort, msd_radix_sort
from algorithms import natural_sort, patience_sort, tree_sort

# Map sorting algorithm names to their respective implementations
algorithmsDict = {
    'insertionSort'       : insertionSort,                                                              #1
    'bubbleSort'          : bubbleSort,                                                                 #2
    'selectionSort'       : selectionSort,                                                              #3
    'mergeSort'           : mergeSort,                                                                  #4
    'quickSort'           : quickSort,                                                                  #5
    'countingSort'        : countingSort,                                                               #6
    'cocktailSort'        : cocktailSort,                                                               #7
    'cycleSort'           : cycleSort,                                                                  #8
    'bogoSort'            : bogoSort,                                                                   #9
    'heapSort'            : heapSort,                                                                   #10
    'radixSort'           : radixSort,                                                                  #11
    'shellSort'           : shellSort,                                                                  #12
    'gnomeSort'           : gnomeSort,                                                                  #13
    'combSort'            : combSort,                                                                   #14
    'bitonicSort'         : bitonicSort,                                                                #15
    'pancakeSort'         : pancakeSort,                                                                #16
    'binaryInsertionSort' : binaryinsertionSort,                                                        #17
    'bucketSort'          : bucketSort,                                                                 #18
    'timSort'             : timSort,                                                                    #19
    'stoogeSort'          : stoogeSort,                                                                 #20
    'strandSort'          : strandSort,                                                                 #21
    'oddEvenSort'         : oddevenSort,                                                                #22
    'pigeonholeSort'      : pigeonholeSort,                                                             #23
    'exchangeSort'        : exchangeSort,                                                               #24
    'treeSort'            : treeSort,                                                                   #25
    'slowSort'            : slowSort,                                                                   #26
    'beadSort'            : beadSort.beadSort,                                                          #27
    'circleSort'          : circle_sort.circleSort,                                                     #28
    'doubleSort'          : double_sort.doubleSort,                                                     #29
    'introSort'           : intro_sort.intro_sort_visualizer,                                           #30
    'iterativeMergeSort'  : iterative_merge_sort.iter_merge_sort_gen,                                   #31
    'mergeInsertionSort'  : merge_insertion_sort.merge_insertion_sort_gen,                              #32
    'msd-RadixSort'       : msd_radix_sort.msdRadixSort,                                                #33
    'naturalSort'         : natural_sort.naturalSort,                                                   #34
    'patienceSort'        : patience_sort.patience_sort_visualize,                                      #35
    'treeSort'            : tree_sort.tree_sort_visualize
}
