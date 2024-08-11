#zkusil jsem jit na to "od lesa". Pouzil jsem dekoratory pro lepsi citelnost kodu
#cely kod jsem udelal dynamicky, kdy je rozdelen na sekvence, ktere jdou rozsirovat
#cely kod je komentovan tak jak jsem mel myslenkovy pochod a vysvetluji jednotlive casti


#________________________________________________________

class SadaCisel:
    def __init__(self, cisla=None):#pokud neni nacte se prazdny

        self.cisla = cisla if cisla else []

    @property
    def soucet(self):#soucet, klasika

        return sum(self.cisla)

    @property
    def prumer(self):#prumer

        return self.soucet / len(self.cisla) if self.cisla else 0

    @property
    def maximum(self): #vraci nejvetsi prvek v sade. /default=none/

        return max(self.cisla, default=None)

    @property
    def minimum(self): #vraci nejmensi prvek v sade

        return min(self.cisla, default=None)

def nacti_cisla():#nacitani vstupu uzivatele

    cisla = []
    print("Zadejte čísla nebo pro ukončení napište 'konec'.")
    while True:
        vstup = input("Zadejte číslo: ")
        if vstup.strip().lower() == 'konec':
            break
        try:
            cislo = int(vstup)
            cisla.append(cislo)
        except ValueError:
            print("Opakujte.")
    return cisla

def zobraz_menu(sada):#rutina menu

    while True:
        print("\nVyberte operaci:")
        print("1. Součet")
        print("2. Průměr")
        print("3. Maximum")
        print("4. Minimum")
        print("5. Konec")

        volba = input("Zadejte volbu (1-5): ")

        if volba == '1':
            print(f"Součet: {sada.soucet}")
        elif volba == '2':
            print(f"Průměr: {sada.prumer}")
        elif volba == '3':
            maximum = sada.maximum
            print(f"Maximum: {maximum}" if maximum is not None else "Empty.")
        elif volba == '4':
            minimum = sada.minimum
            print(f"Minimum: {minimum}" if minimum is not None else "Empty.")
        elif volba == '5':
            print("Konec.")
            break
        else:
            print("Opakovat.")

def main():

    cisla = nacti_cisla()
    sada = SadaCisel(cisla)
    zobraz_menu(sada)

if __name__ == "__main__":
    main()

