from Converter import Converter


class ConverterLibrary(object):
    value = 0

    def __init__(self):
        self.converter = Converter(eur = 5)

    def test_usd(self):  # keyword
        self.value = self.converter.eur_to_usd()

    def test_mkd(self):  # keyword
        self.value = self.converter.eur_to_mkd()

    def test_chf(self):  # keyword
        self.value = self.converter.eur_to_chf()

    def test_dem(self):  # keyword
        self.value = self.converter.eur_to_dem()

    def result_should_be(self,expected_value):  # keyword
        if self.value != expected_value:
            raise AssertionError('%s != %s' % (self.value, expected_value))

converter = ConverterLibrary()
converter.test_usd()
print(converter.value)
