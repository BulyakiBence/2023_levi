def oszthato(szam):
    if szam % 7== 0 and szam % 3 != 0:
        return True
    else:
        return False
osszes = 0
darab = 0
for szam in range (100,1000):
    if oszthato(szam):
        osszes += szam
        darab += 1

atlag = osszes/darab
print(f"Átlaguk: {atlag:.2f}")