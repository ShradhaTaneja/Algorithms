print 'enter the number of elements '
n = input()
print 'enter the elements - seperate by a space'
arr = list(map(int, raw_input().split(' ')))

if len(arr) > n:
    print 'invalid number of elements have been entered. retry.'
    exit()

arr = [5, 2, 8, 6, 1, 10]
#print list(reversed(arr[1:4])) # prints item from 1 to 3

def insertion_sort(l):
    for j in range(1, len(l)):
        print 'j = ', j
        print arr
        key = l[j]
        i = j-1
        print 'i = ', i
        print arr
        while i>=0 and l[i] > key:
            l[i+1] = l[i]
            l[i] = key
            i = i - 1
            print 'inside while arr = ', arr

insertion_sort(arr)
print '-----\n', arr

