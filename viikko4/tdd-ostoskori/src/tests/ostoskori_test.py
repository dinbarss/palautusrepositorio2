import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.mehu = Tuote("Mehu", 5)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), self.maito.hinta())

    def test_kahden_erilaisen_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.mehu)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_erilaisen_tuotteen_hinta_on_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.mehu)

        self.assertEqual(self.kori.hinta(), self.maito.hinta() + self.mehu.hinta())

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_hinta_on_kaksinkertainen(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 2 * self.maito.hinta())
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(self.kori.hinta(), 3)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostokset_lista_sisaltaa_yhden_ostoksen(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_jalkeen_ostoksella_oikea_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)
        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_erilaisen_tuotteen_jalkeen_ostoksia_on_kaksi(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.mehu)

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tuotteen_jalkeen_ostoksia_on_tasan_yksi(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_saman_tuotteen_jalkeen_ostoksella_oikea_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 2)

    def test_yhden_saman_tuotteen_poiston_jalkeen_ostoksen_maara_on_yksi(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 1)

    def test_tuotteen_lisaamisen_ja_poistamisen_jalkeen_kori_on_tyhja(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)

    def test_tyhjenna_tyhjentaa_korin(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.mehu)
        self.kori.tyhjenna()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)