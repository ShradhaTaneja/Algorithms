print 'enter the number of elements'
v = input()

data = {}

def memo_fib(n):
    try:
        n_minus_one = data[n-1]
    except:
        return memo_fib(n-1)

    try:
        n_minus_two = data[n-2]
    except:
        return memo_fib(n-2)

    return n_minus_one + n_minus_two


def fib_recursive(n):
    if n == 0 or n == 1:
        return 1
    ans = fib_recursive(n-1) + fib_recursive(n-2)
    return ans


for a in range(0, v):
    print memo_fib(a)


