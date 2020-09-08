# Insertion Sort Algorithm
#Code Ref: https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheInsertionSort.html

def insertionSort(alist):
    for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
    return alist