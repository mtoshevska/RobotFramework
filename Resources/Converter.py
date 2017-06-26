class Converter:
    eur = 0

    def __init__(self,eur):
        self.eur = eur

    def __str__(self):
        return str(self.eur)

    def eur_to_usd(self):
        return self.eur*1.12

    def eur_to_mkd(self):
        return self.eur*61.69

    def eur_to_chf(self):
        return self.eur*1.09

    def eur_to_dem(self):
        return self.eur*1.92

# money = Converter(eur=2)
# print(money)
