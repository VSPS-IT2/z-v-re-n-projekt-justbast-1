ukoly =[] #List kde se úkoly přidávají

def pridani_ukolu(ukoly): #Funkce která umožňuje uživateli přidat úkol pomoci uživatelských vstupů a proměnných
    
    nazev = input("Zadejte název úkolu:")
    popisek = input("Zadejte popisek k úkolu, ať víte co máte udělat:  ")
    cas = input("Zadejte platnost úkolu: ")
    #ukoly= print("Název úkolu: " + nazev + "\nPopis: " + popisek + "\nČas platnosti: " + cas)
    ukoly.append("|Název:  " +  nazev + " |Popis:  " +popisek+ "  |Čas:  " +cas) #Funkce append umožňuje přidat daný úkol do listu
    print("Úkol byl přidán!")


def zobrazeni_ukolu(ukoly):  # funkce pro zobrazení úkolů
    if ukoly:
        print("Úkoly: ")
        for index, ukol in enumerate(ukoly, start=1): #Tento cyklus nám umožňuje ukládat jednotlivé úkoly do seznamu s default indexem 1 a né 0
            print(f"{index}. {ukol}")
    else:
        print("Žádné úkoly")
           
            

print("Vítejte ve správci úkolů")
while True: #Použití cyklu pro neustálé přidávání nových úkolů a zobrazování
 print("Stisknutím klávesy 'A' můžete přidat nový úkol, stisknutím 'T' zobrazíte úkoly")

 znak = input("Zadejte klávesu pro přidání nového úkolu: ")
 znak = znak.upper() #zde byla přidána funkce upper kdyby uživatel náhodou zadal malý znak tak se automaticky přemění na velký, tím pádem to proběhne bez chyb
 if znak == 'A':    
    pridani_ukolu(ukoly)

 elif znak == 'T':
    zobrazeni_ukolu(ukoly)  
    
 else:
    print("Špatná klávesa")

