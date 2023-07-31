def stepen(a,b):
    if b == 0:
        return 1
    return a*stepen(a,b-1)
chislo_a = int(input("введите число а: "))
chislo_b = int(input("введите число b: "))
print(stepen(chislo_a,chislo_b))