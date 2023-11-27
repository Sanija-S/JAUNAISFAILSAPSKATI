"""


(fails+ režīms)

"""


fails=open("aka.txt", "a", encoding="utf-8")
fails.write("Ār šo funkciju tiek ierakstīts failā teksts")

fails.close() # neaizmirsti aizvert failu

# atvert un nolasit(down arrows)

ff=open("aka.txt","r", encoding="utf-8")
print(ff.read())



#izveidot jaunu tuksu failu
gg=open("Ziema.txt","x", encoding="utf-8")# ar   encoding="utf-8"    pievieno latviesu rakst zimes
kk=open("vasara.txt", "w")# ja tas eksistes vins atvers rakstisanas rezimaa


# džēšama- jaimporte modulis (os)- nodrosina funkcijas ar operatorsistemu, neatkarigi kada sistema...windows utt
import os
os.remove("ziema.txt") #remove ja grib dzēst, ja nav rada kas nav

# kā pārbauda, vai fails neeksistē
import os
if os.path.exists("aka.txt"):
    os.remove("aka.txt")
else:
    print("Fails neeksistē")
# ja rodas sada situacija- lai izvairotos no kludas, parbaudi vai fails pastāv, un tad to dzēst arā- 