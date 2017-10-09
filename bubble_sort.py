arr = [5, 2, 8, 6, 1, 10]



# start by moving maximum value to the right at each iteration
def bubble_sort_2(arr):
    swap = -1
    sorted_len = len(arr) - 1
    while (swap != 0):
        swap = 0
        for i in range(0, sorted_len):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
                swap += 1
        sorted_len -= 1
    return arr


# compare values with two for loops
def bubble_sort_1(arr):
    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1, i, -1):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


#print arr

print bubble_sort_1(arr)
#print bubble_sort_2(arr)


#print arr

