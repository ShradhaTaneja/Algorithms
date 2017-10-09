print 'enter the number of elements '
n = input()
print 'enter the elements - seperate by a space'
arr = list(map(int, raw_input().split(' ')))

arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
#arr = [6, 3, 8, 12, 1, 2, 34, 5, 7]
arr = [-1] + arr

def heapify(arr, i, order = 'max'):
    l = 2*i
    r = 2*i + 1
    largest_index = i
    print '\n calling heapify on ', arr[i]

    len_arr = len(arr) - 1

    if l<=len_arr and arr[l] > arr[largest_index]:
#        print arr[l], arr[largest_index]
        largest_index = l
#        print largest_index, '++++'

    if r<=len_arr and arr[r] > arr[largest_index]:
#        print arr[r], arr[largest_index]
        largest_index = r
#        print largest_index, '++++'

#    print largest_index, '......'

    if largest_index != i:
        # swap parent with largest child
        arr = swap(arr, i, largest_index)
#        print 'swapped ', arr[largest_index], arr[i]
#        print 'calling heapify on ', largest_index
        print 'after heapify - ', arr[1:]
        heapify(arr, largest_index)


def build_heap(arr, order = 'max'):
    len_arr = len(arr) - 1
    for index in range(len_arr/2, 0, -1):
        heapify(arr, index)
    print '\n\n After Build Heap ', arr[1:]

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr

def heap_sort(arr, order = 'max'):
    len_arr = len(arr) - 1
    sorted_arr = []
    print 'Given Array : ', arr[1:]
    build_heap(arr)

#    while (arr):
#        build_heap(arr)
#        arr = swap(arr, 1, len(arr))
#        max_item = arr.pop()
#        sorted_arr.append(max_item)
#        heapify(arr, 1)

    for i in range(len_arr, 0, -1):
        arr = swap(arr, 1, i)
        max_item = arr.pop()
#        print max_item, '<<'
        sorted_arr.append(max_item)
        heapify(arr, 1)
    return sorted_arr

print heap_sort(arr)
