# Write a program which, repeatedly, reads integers, until the user enters "done".
# Once "done" is entered, print out the total, count, and average, of the integers.
# If the user enters anything other than integers, detect their mistake using
# try and except, and print an error message, and skip to the next integers.

num = 0
tot = 0.0

while True :

    sval = input('Enter a number: ')

    if sval == 'done' :
        break

    try:
        fval = float(sval)

    except:
        print('Invalid input')
        continue

    num = num + 1

    tot = tot + fval

print(tot,num,tot/num)