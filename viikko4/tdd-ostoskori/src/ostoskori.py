from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # the shopping cart stores Ostos objects, one per Tuote in the cart
        self._ostokset = []

    def tavaroita_korissa(self):
        # tells the number of items in the cart
        # if 2 items of the product "maito" have been added to the cart,
        #   the method should return 2
        # if the cart has 1 item of the product "maito" and 1 item of the product "juusto",
        #   the method should return 2
        return sum(ostos.lukumaara() for ostos in self._ostokset)

    def hinta(self):
        # tells the total price of the purchases in the cart
        return sum(ostos.hinta() for ostos in self._ostokset)

    def lisaa_tuote(self, lisattava: Tuote):
        # adds the product
        ostos = self._hae_ostos(lisattava)
        if ostos:
            ostos.muuta_lukumaaraa(1)
            return
        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # removes the product
        ostos = self._hae_ostos(poistettava)
        if ostos:
            ostos.muuta_lukumaaraa(-1)
            if ostos.lukumaara() <= 0:
                self._ostokset.remove(ostos)

    def tyhjenna(self):
        # empties the shopping cart
        self._ostokset = []

    def _hae_ostos(self, tuote: Tuote):
        for ostos in self._ostokset:
            if ostos.tuotteen_nimi() == tuote.nimi():
                return ostos
        return None

    def ostokset(self):
        # returns a list of the Ostos objects in the cart
        # so each Ostos object tells which product it is about
        #   AND how many items of that product are in the cart
        return self._ostokset