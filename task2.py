"""
Write the recursive function that will form a patterns starting from positive integer number N
with step M. Function should print numbers in descending order starting from N
with step M until it becomes negative or zero.
After it becomes negative or zero it should return back to the originating number N
with same step M.

Examples: N = 15 M = 5 Output: 15 10 5 0 5 10 15
"""
#
# def f(N,M):
#
#     if N <= M:
#         return str(N)
#
#
#     niz1 = f(N-M, M) + " " + str(N)
#
#     niz2 = str(N) + ' ' + f(N-M, M)
#
#     return niz1
#
# print(f(17,5))
def rekurzija(x, stepen):

    if stepen < 0:

        if x > 0:
            rec(x-1, stepen)
        else:
            rec(x+1, stepen)
    else:
        if x < n:
            rec(x + n, stepen)
        else:
            return

N = int(input("N: "))

M = int(input("M: "))
rekurzija(N,M)