# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(0, len(merged_arr)):
        # if all elements in arrA have been merged put next element in arrB into merged array
        # if all elements in arrB have been merged put next element in arrA into merged array
        if len( arrA ) < 1:
            merged_arr.append(arrB)
        elif len(arrB) < 1:
            merged_arr.append(arrA)
        elif arrA[i]< arrB[i] :
            val = arrA.pop(i)
            merged_arr.append(val)
        elif arrA[i] > arrB[i]:
            val = arrB.pop(i)
            merged_arr.append(val)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # 1. While your data set contains more than one item, split it in half
    if len(arr) > 1:
        left = merge_sort(arr[ 0 : int(len(arr)/ 2)])
        right = merge_sort(arr[ int(len(arr)/2):])
        arr = merge(left, right)
    return arr
l = [1,2,5,4,7]
merge_sort(l)


# 2. Once you have gotten down to a single element, you have also *sorted* that element 
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled




# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr):

    return arr



# Quick Sort

def quicksort ( arr, low, high  ):
    if low >= high:
        return arr
    else:
        pivot_index = low
        for i in range(low, high):
            if arr[i] < arr[pivot_index]:
                temp = arr[pivot_index+1]
                arr[pivot_index+1] = arr[i]
                arr[i] = temp

                temp = arr[pivot_index]
                arr[pivot_index] = arr[pivot_index+1]
                arr[pivot_index] = temp
                pivot_index +=1
    arr = quicksort(arr, low, pivot_index)
    arr = quicksort(arr, pivot_index+1, high)

    return arr
            



