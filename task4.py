"""
Write a most efficient function insert() that inserts integer number into the already sorted
array. After the insertion the array should stay sorted. Explain your approach in comments.
Calculate complexity for your algorithm considering worst case scenario - give answer in
comments.

"""

def insert(niz, num):

    niz2 = []

    for i in range(len(niz)):

        if niz[i] < num or niz[i] > num:
            niz2.append(niz[i])

        else:
            niz2.append(num)


    return niz2


print(insert([1,2,6,7],4))