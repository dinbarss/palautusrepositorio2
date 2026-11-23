import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_tuotteen_hinta(self):
        maito = Tuote("maito", 3)

        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), maito.hinta())

    def test_kahden_erilaisen_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("maito", 3)
        mehu = Tuote("mehu", 5)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(mehu)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_erilaisen_tuotteen_hinta_on_tuotteiden_hintojen_summa(self):
        maito = Tuote("maito", 3)
        mehu = Tuote("mehu", 5)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(mehu)

        self.assertEqual(self.kori.hinta(), maito.hinta() + mehu.hinta())

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_hinta_on_kaksinkertainen(self):
        maito = Tuote("maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 2 * maito.hinta())
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(self.kori.hinta(), 3)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostokset_lista_sisaltaa_yhden_ostoksen(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_jalkeen_ostoksella_oikea_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_erilaisen_tuotteen_jalkeen_ostoksia_on_kaksi(self):
        maito = Tuote("Maito", 3)
        mehu = Tuote("Mehu", 5)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(mehu)

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tuotteen_jalkeen_ostoksia_on_tasan_yksi(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_saman_tuotteen_jalkeen_ostoksella_oikea_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 2)

    def test_yhden_saman_tuotteen_poiston_jalkeen_ostoksen_maara_on_yksi(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 1)