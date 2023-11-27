
"""
read()
- atgirez visu info, 
ja ievieto 23 tad nolasa pirmos 3 simbolus

readline()- nolasa 1 rindiņu
"""

fails= open("testadatne.txt", "r", encoding="utf-8")
print(fails.read(3))
# pārlokot visu failu pa rindinaam!(vispirms 1st rindu ...tad 2nd utt...)- CIKLA KONSTRKCIJA FOR
for ii in fails:
    print(ii)

fails.close()