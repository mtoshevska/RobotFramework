from Converter import Converter


class ConverterLibrary(object):
    value = 0

    def __init__(self):
        self.converter = Converter(eur = 5)
        self.value = 0

    def test_usd(self):  # keyword
        self.value = self.converter.eur_to_usd()

    def test_mkd(self):  # keyword
        self.value = self.converter.eur_to_mkd()

    def test_chf(self):  # keyword
        self.value = self.converter.eur_to_chf()

    def test_dem(self):  # keyword
        self.value = self.converter.eur_to_dem()

    def result_should_be(self,expected_value):  # keyword
        if str(self.value) != expected_value:
            raise AssertionError('%s != %s' % (self.value, expected_value))

converter = ConverterLibrary()
converter.test_usd()
print('USD: %s' % converter.value)
converter.test_mkd()
print('MKD: %s' % converter.value)
converter.test_chf()
print('CHF: %s' % converter.value)
converter.test_dem()
print('DEM: %s' % converter.value)
