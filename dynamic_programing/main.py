'''Dynamic problem
A method for solving a complex problem by breaking it down into collection
of simpler subproblems, solving each of those subproblems just once and 
storing the solution

ONLY WORKS IF:

1. Optimal structure: 
2. Overlapping subproblems: If it can be broken down into subproblems which 
   are reused several times.


Tabulation:
Also it is used to resolve the fib problem, storing the result of a previous 
result in a "table" (usually arrays), usually done using iteration, better
space complexity can be achieved using tabulation   
'''


def fib(n):
    '''Time complexity: O(2*n)'''
    if n <= 2: return 1
    return fib(n - 1) + fib(n - 2)


print(fib(6))


def fib_memo(n, memo={}):
    '''Time complexity: O(N)'''

    if n in memo: return memo[n]
    if n <= 2: return 1
    
    next_loop = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    memo[n] = next_loop

    return next_loop


print(fib_memo(5))


def fib_tabulation(n):
    if n <= 2: return 1

    fib_numbers = {
        '0': 0,
        '1': 1,
        '2': 1
    }

    for idx in range(len(fib_numbers.keys()), n + 1):           
        fib_numbers[str(idx)] = fib_numbers[str(idx - 1)] + fib_numbers[str(idx - 2)]

    return fib_numbers[str(n)]


print(fib_tabulation(6))    