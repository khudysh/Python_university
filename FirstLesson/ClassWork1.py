def first():
    for i in range(100, 1000):
        x = i ** 2
        if i == (x % 1000):
            print(i, "\t")

def second(n):
    for i in range(100, 1000):
        sum = 0
        saveI = i
        while saveI > 0:
            sum += saveI % 10
            saveI //= 10
        if (n == sum):
            print(i)

def third(A, B):
    for i in range(A, B):
        tmp = str(i)
        if (str(i) == tmp[::-1]):
            print(i)

def fourth(A, B):
    for i in range(A, B):
        tmp = str(i)
        for j in tmp:
            if (tmp.count(j) == 3):
                print(i)
                break;


#first()

#n = int(input())
#second(n)

#A = int(input())
#B = int(input())
#third(A, B)

A = int(input())
B = int(input())
fourth(A, B)
