"""

stradaju ar failu zem.txt

Izveidot datni zem.txt, kurā ir teksts,   #izveidoju failu ar tekstu
nolasit tekstu, izdrukajot termiālī,      #var stradat ar try un except,  
                                           vai ar vieglāku- "with open"
                                           nosaka to kurur funkciju gribu lai veic- "r"


noteikt simbolu skaitu tajā, burti, ciparu, interpunkcijas zīmes 
                                    #skat. 22-24 rindu

izdrukāt pirmos 10 simbolus,    #skat. 25-26 rindu
izdrukāt pirmo un pēdejo simbolu #skat. 27-30 rindu

"""

with open ("zem.txt", "r", encoding="utf8") as datne:
    teksts=datne.read() #mainigais kas nolasa/ norāda visu tekstu
    print(f"Failā ir šāds teksts{teksts}")
    # zdrukat simbolu skaitu, simbolu virnes garums ar len
    skaitls=len(teksts)
    print(f"Simbolu skaits tekstā ir {skaitls}.")
    #izdrukā pirmos 10 simbolus
    print(f"Pirmie 10 simboli ir: {teksts[:10]}.")# var ar KVADRAT IEKAVAM acutally noradit cik simbolus izrintee
    # idrukat 1 un pedejo simbolu. jāzin kā indeksēt simbolus virknē
    # indeksācija- katram simbolam ir sava vieta virknē
    # ziema  z=0, i=1, e=2..., a(or last simbol)=-1
    print(f"Pirmais un pēdejais simbols ir: {teksts[0]} {teksts[-1]}")


    # var ievadīt teminālī, un tas ieinstele biobliotēku?-    pip install cryptography 

# updatot versiu var ar:     python.exe -m pip install --upgrade pip


