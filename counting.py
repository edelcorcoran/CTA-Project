# Counting Algorithm
# Code Ref: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php


def countingSort(array1):
    m = 100 + 1
    count = [0] * m                
    
    for a in array1:
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            array1[i] = a
            i += 1
    return array1