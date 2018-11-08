"""
Find the mean value of the `special` integer numbers provided by the user input. The number is considered `special` if
it divisible by 3 but not divisible by 5. User should be allowed to input numbers until `=` sign is entered as input.
After `=` is entered program should print mean value of the entered `special` numbers.

**Note:** It is not allowed to use list/arrays or `sum()` in order to solve this task.

"""

suma = 0
broj =0
while True:
    num = input("Unesi broj ili =: ")

    if num !='=':

        if int(num) % 3==0 and int(num) % 5 !=0:

            suma += int(num)
            broj +=1
    else:

        print("Rezultat je " + str (suma/broj) + ".")
        break

