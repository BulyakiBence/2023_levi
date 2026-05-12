class Nagykonyv:
    def __init__(self,nev,szulev,halev,nemz,cim,hely):
        self.nev = nev
        self.szulev = int(szulev)
        self.halev =int( halev)
        self.nemz = nemz
        self.cim = cim
        self.hely = int(hely)

fajl = open("2023/Forrasok/02_feladat/konyvek.txt", "r", encoding="utf-8")
fajl.readline()
konyvek = []
for sor in fajl:
    adatok = sor.strip().split(";")
    uj = Nagykonyv(
                    adatok[0],
                    adatok[1],
                    adatok[2] if adatok[2] != "" else 2005,
                    adatok[3],
                    adatok[4],
                    adatok[5]

    )
    konyvek.append(uj)

fajl.close()

#3.2 feladat
print(f"Ennyi konyv szerepel az allomanyban: {len(konyvek)}")

#3.3 feladat
magyarok = [k for k in konyvek if k.nemz == "magyar"]

if magyarok:
    legjobb_konyv = magyarok[0] # Az első magyartól indulunk
    for konyv in magyarok:
        if konyv.hely < legjobb_konyv.hely:
            legjobb_konyv = konyv
    
    print(f"A legjobb helyezést elért magyar könyv: {legjobb_konyv.nev}, {legjobb_konyv.cim}")

#3.4 fel
van = False
for k in konyvek:
    if k.nemz == "német":
        van = True

if van == True:
    print("Szerepel német író könyve")
else:
    print("Nm szerepel")

#3.5 fel
kilencv = []
for konyv in konyvek:
    if(konyv.halev - konyv.szulev >90):
        if konyv.nev not in kilencv:
            kilencv.append(konyv.nev)
for iro in kilencv:
    print(iro)