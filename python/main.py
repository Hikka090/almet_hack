import bacdive
import sys

f = open('text.txt', 'w')

client = bacdive.BacdiveClient("valera.lesnikov.09@gmail.com", "Hikka090")
count = client.search(taxonomy="Staphylococcus haemolyticus")

print(count, 'strains found.')
for strain in client.retrieve(['keywords', 'culture collection no.']): 
        print("\n", strain, file=f)
        print("\n", strain)             
f.write(str(input("")))     
f.close()