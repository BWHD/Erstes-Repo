class Auto:
    anzahl_räder = 0
    farbe = ""
    hersteller = ""

    def  __init__(self, anzahl_räder, farbe, hersteller):
        self.anzahl_räder= anzahl_räder
        self.farbe = farbe
        self.hersteller = hersteller



auto1 = Auto(4, "rot", "Audi")
auto2 = Auto(4, "blau", "BMW")
auto3 = Auto(4, "gruen", "Tesla")

print(auto1.hersteller)
print(auto2.farbe)