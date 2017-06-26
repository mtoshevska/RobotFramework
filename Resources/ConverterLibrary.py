from Resources import Converter


class ConverterLibrary:
    value = 0

    def __init__(self):
        self.converter = Converter.Converter(eur = 5)

    def test_usd(self):  # keyword
        self.value = self.converter.eur_to_usd()

    def test_mkd(self):  # keyword
        self.value = self.converter.eur_to_mkd()

    def test_chf(self):  # keyword
        self.value = self.converter.eur_to_chf()

    def test_dem(self):  # keyword
        self.value = self.converter.eur_to_dem()

# c = ConverterLibrary()
# c.test_usd()
# print(c.value)
