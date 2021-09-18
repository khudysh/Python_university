def first():
    listOfNumbers = input().split()
    listOfNumbers = list(map(int, listOfNumbers))

    counter = 1
    max = 0
    for i in range(1,len(listOfNumbers)):
        if(listOfNumbers[i] == listOfNumbers[i-1]):
            counter+=1
        else:
            if (max < counter):
                max = counter
            counter = 1
    print("MAX:", max)


def second():
    listOfNumbers = input().split()
    listOfNumbers = list(map(int, listOfNumbers))

    counter = 1
    bigger = 0
    less = 0
    for i in range(1, len(listOfNumbers)):
        if (listOfNumbers[i] > listOfNumbers[i - 1]):
            counter += 1
            #print("pr: ", counter)
            bigger = max(counter, bigger)
        else:
            bigger = max(counter, bigger)
            counter = 1
    counter = 1
    for i in range(1, len(listOfNumbers)):
        if (listOfNumbers[i] < listOfNumbers[i - 1]):
            counter += 1
            #print("vt: ", counter)
            less = max(counter, less)
        else:
            less = max(counter, less)
            counter = 1
    print(max(less, bigger))

def third():
    listOfNumbers = input().split()
    listOfNumbers = list(map(int, listOfNumbers))

    counter = 0
    for i in range(1, len(listOfNumbers)-1):
        if (listOfNumbers[i] > listOfNumbers[i - 1] and listOfNumbers[i] > listOfNumbers[i + 1]):
            counter += 1

    print(counter)

def fourth():
    listOfNumbers = input().split()
    listOfNumbers = list(map(int, listOfNumbers))

    counter = 0
    for i in range(1, len(listOfNumbers)-1):
        if (listOfNumbers[i] > listOfNumbers[i - 1] and listOfNumbers[i] > listOfNumbers[i + 1]):
            counter += 1

    print(counter)

#
# for i in str
#     try:
#         mas.append(int(i))
#     except:
#         pass

