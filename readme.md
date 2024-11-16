# 7. Feladat: Siklóernyő (72 pont)

Alex siklóernyőzni szeretne a Tátra hegycsúcsain. A hegycsúcsok a Tátrában négyzetrácsosan **N** sorban és azon belül **M** oszlopban helyezkednek el, és mindegyiknek ismert a magassága. A siklóernyőzés során Alex elindul az egyik kiválasztott hegycsúcsról, és átrepül valamelyik (nem feltétlenül szomszédos) alacsonyabb magasságú hegycsúcsra, mely a jelenlegi csúccsal azonos sorban vagy azonos oszlopban helyezkedik el.

A csúcsokat nem szükséges közvetlenül átrepülnie (a levegőben elkerülheti a közbeeső magasabb hegycsúcsokat). A repülések során Alex több alkalommal is átrepülhet, és bármelyik csúcsról befejezheti a siklóernyőzést, ha legalább egy alkalommal már átrepült.

Add meg a lentebb megadott magasságok esetén minden egyes hegycsúcsra, hogy onnan kiindulva:

## A) Hány különböző siklóernyőzést tehet, mely során pontosan egy alkalommal repül át másik csúcsra?

## B) Hány különböző siklóernyőzést tehet, mely során pontosan két alkalommal repül át másik csúcsra?

## C) Hány különböző siklóernyőzést tehet összesen?

### Bemenet:

- Az első sorban két egész számot olvashatunk: **N** (a sorok száma) és **M** (az oszlopok száma).
- A következő **N** sor mindegyike **M** egész számot tartalmaz, amelyek a hegycsúcsok magasságát jelzik.

### Kimenet:

- Az első sorban a válasz a pontosan egy átrepüléssel végrehajtható siklóernyőzések számát adja meg.
- A második sorban a válasz a pontosan két átrepüléssel végrehajtható siklóernyőzések számát adja meg.
- A harmadik sorban a válasz az összes lehetséges siklóernyőzés számát adja meg.

### Példa bemenet:

3 4 1 1 3 5 1 1 1 4 9 2 7 6

### Példa kimenet:

6 2 10

### Magyarázat:

A bemenet szerint egy 3x4-es mátrixot kapunk, amelyben az egyes csúcsok magasságai szerepelnek. A feladatban meghatározott, hogy milyen módon lehet elérni másik csúcsokat a szabályok szerint. Az eredmények alapján a következő számokat kaptuk:

- Az első sor a pontosan egy átrepüléssel elérhető utak számát.
- A második sor a pontosan két átrepüléssel elérhető utak számát.
- A harmadik sor az összes lehetséges repülési mód számát tartalmazza.
