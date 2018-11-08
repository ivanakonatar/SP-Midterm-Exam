"""
Write a script that calculates sum of the products of the elements on the main and the secondary
matrix diagonal. Calculate algorithm complexity - give answer in comments.
"""

m = int(input("Unesite red matrice: "))
A = []

for i in range(m):
    x = []
    for j in range(m):
        a = int(input("Unesi elemente matrice redom: "))
        x.append(a)
    A.append(x)


main_d = 1
for i in range(m):
    main_d *= A[i][i]


secondary_d = 1
for i in range(m):
    for j in range(m):
        if i+j == m - 1:
            secondary_d *= A[i][j]


for i in A:
    print(i)


print("Rezultat je " + str(main_d + secondary_d) + ".")

#kompleksnost je 2n + 1