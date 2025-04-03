class TestPrismaTrapezoidal(unittest.TestCase):
    def test_creacion_prisma(self):
        prisma = PrismaTrapezoidal(base_mayor=8, base_menor=4, lado=5, altura_trapecio=3, altura_prisma=10)
        self.assertEqual(prisma.base_mayor, 8)
        self.assertEqual(prisma.altura_prisma, 10)

    def test_valores_negativos_error(self):
        with self.assertRaises(ValueError):
            PrismaTrapezoidal(base_mayor=-8, base_menor=4, lado=5, altura_trapecio=3, altura_prisma=10)

    def test_volumen(self):
        prisma = PrismaTrapezoidal(base_mayor=8, base_menor=4, lado=5, altura_trapecio=3, altura_prisma=10)
        # Volumen = Área_base * altura_prisma
        # Área_base = ((8 + 4)/2) * 3 = 18
        # Volumen = 18 * 10 = 180
        self.assertAlmostEqual(prisma.volumen(), 180, places=3)

    def test_area_superficial(self):
        prisma = PrismaTrapezoidal(base_mayor=8, base_menor=4, lado=5, altura_trapecio=3, altura_prisma=10)
        # Área = (B + b)*h + (B + b + 2d)*H
        # (8+4)*3 + (8+4+2*5)*10 = 36 + (22)*10 = 36 + 220 = 256
        self.assertAlmostEqual(prisma.area_superficial(), 256, places=3)

