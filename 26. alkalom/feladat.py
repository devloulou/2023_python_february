OOP feladat:

1 bolt kassza programját kellene megírni.

A program előre meghatározott árukészlettel rendelkezzen.
Ezt nem kell túl gondolni: pl. tej, kenyér, csoki stb.

Minden terméknek legyen egy általad választott ára: akár randomizált módon is lehet

Minden boltnak van 1 raktár készlete, ennek kialakítása, feltöltése a program elején történjen meg.
Ezt sem kell túlgondolni:
pl. kenyér 4 db, csoki 5 db stb.

A kassza képes legyen arra, hogy az ember által összeválogatott termékeket 
eladni tudja.

Folyamat: lesz egy általad megadott beváráslókosár - pl. egy listában legyenek benne a termékeket
Ezeket akarod megvenni a boltból.

A művelet végén jelenjen meg egy blokkon, hogy miből mennyit vásároltunk
mennyit fizettünk
és ha belefér, akkor mennyi ennek a bruttó értéke - 18%-os adóteherrel számoljunk 

A feladat során amit látni szeretnék: osztályokban van szervezve a termékek 
a raktárkészlet 
és a kassza

Minden egyéb feladat lehet teljesen manuálisan megadva.

példa a program használatára:

if __name__ == '__main__':
	kassza = Kasszaosztály()		
	kosaram = [tej, kenyér, csoki] -> a termékek is egy osztállyal vannak megvalósítva	
	
	blokk = kassza.sell(kosaram)	
	
	print(blokk) -> 3 kenyér - 400 Ft / db
					2 csoki - 450 ft / db
					
					összesen: 2100 Ft net,
					összesen bruttó: 2100 *1.18
	