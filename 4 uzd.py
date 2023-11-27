"""

no terminala jautat "Īevadi savu dardu"" , 
vards tiek ierakstits failaa "rudens.txt"

1.0 lietotajam tiek lugts ievadit vardu
"""



vards=input("ievadīt savu vārdu:")
faila_nosaukums= "rudens.txt"
try:
  with open(faila_nosaukums, "w") as ff: # w- ierakstīit, nodzesis visu un ievadis par jaunu
     ff.write(vards)
     print(f"vards {vards}ir ierakstīts failā {faila_nosaukums}")
   # megina atvert failu un ierakstit taja vardu- tiklidz ver vaļā tad lieto "try:"
     saturs=ff.read()#seit mes nolasam saturu



except IOError: #iznemumi

   print(f"Nevareja ierakstīt failā{faila_nosaukums}")
   # radijas kluda jo bija w un 16, 18 radis kludu- pasaka ka nevar nolasit failu