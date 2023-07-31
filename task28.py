def sum(a,b):
    if b == 0:
        return a
    return sum(a+1,b-1)
chislo_a = int(input("введите число а: "))
chislo_b = int(input("введите число b: "))
print(sum(chislo_a,chislo_b))