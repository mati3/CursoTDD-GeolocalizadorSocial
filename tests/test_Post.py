import sys, os.path

src = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/src/')
sys.path.append(src)

import unittest

from post import Post

class TestPost(unittest.TestCase):

    # Comprueba que en la ruta devuelve status OK
    def test_create_post(self):
        tags = ["test", "python"]
        p = Post("Federico", tags, "Twitter", "Granada")

        self.assertEqual(p.getAutor(),"Federico", "Autor devuelto incorrecto")
        self.assertEqual(p.getTags(), tags, "Tags devueltos incorrectos")
        self.assertEqual(p.getSocial(),"Twitter", "Red social devuelta incorrecta")
        self.assertEqual(p.getLocation(),"Granada", "Localizacion devuelta incorrecta")
        