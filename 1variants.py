def lasit_datni():
     #ievadīt datnes nosaukumu
    datnes_nosaukums=input("ievadīt datnes nosaukumu:")

    # atvert failu u lasit tas saturu

    try:
       with open (datnes_nosaukums, "r", encoding="utf-8") as fails:
           #c nosaka ka dators izsaka rakst zimes? encoding  utf-8.  as- mainiga nosaukums ko vers valaa?
                #^^^iekavas, ja zinams datnes nosaukums ko rakstitnosaukums var likt datnes nosaukumu, ja nee tad liek mainīgo
            saturs= fails.read()
    
            print(f"datnes saturs ir: {saturs}")
    except FileNotFoundError: #peedinaas liek rezimu, failu atversanai, cetras dazadas metodes(rezimi)
        print("Norādīto failu nevar atrast")
if __name__=="__main__":
   lasit_datni()
  #kadas datnes? .txt, .csv, JSON - teksta datnes, fai;a fprmats kura var ievadit skaitli un simbolus, bet ierobezojums noformejumaa

"""
  "r"- Lasīt(defalt setting), atver sailu lasisanai. ja fails neeksiste met erroru
 "a"- pievienot, jau esosam apend?, atver failu pievienošanai, izveido failu, ja tas neeksistē
 "w" - raksta par jaunu, atver failu rakstisanai, izveido failu
 "x"- izveidot. izveido noradito failu atgriez kludu, ja fails pastāv
 "t"- teksts, noklusejuma vertiba- var nerakstit
 "b"- binarais rezims, atteli teksta vai skaitla forma binaraa
  
  """