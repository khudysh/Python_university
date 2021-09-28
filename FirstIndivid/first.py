import sys

# Переменные
partValues = list()
partAmount = 0

# Функции
def AmountOfPart():
    try:
        partAmount = int(input("Кол-во частиц:"))
    except ValueError:
        print("Введите целое число")
    return partAmount


def AddPart(partAmount):
    print("Введите значение частиц ЯВНО указывая знак (+ или -) иначе числа не будут учитываться:")
    for i in range(partAmount):
        try:
            part = input()
            if(part[0] == '+'):
                partValues.append(int(part[1:]))
            elif(part[0] == '-'):
                partValues.append(-1 * int(part[1:]))
        except:
            print("Вы ввели неправильное значение, придётся вводить всё заново")
            partValues.clear
            AddPart(partAmount)   

def MinMult():
    current = 0
    minim = sys.maxsize
    for current in range(len(partValues)):
        for i in range(len(partValues)):
            minim = min(minim, partValues[i] * partValues[current])
    print(minim)
    
# Программа
partAmount = AmountOfPart()   
AddPart(partAmount)
print(partValues)
MinMult()
