import unittest
from auth import login

class TestAuth(unittest.TestCase):

    # def test_login_success(self):
    #     # Simula un inicio de sesión exitoso
    #     self.assertEqual(login("SarahR", "contra000", "secretaria"), "secretaria")

    # def test_login_failure(self):
    #     # Simula un inicio de sesión fallido
    #     self.assertIsNone(login("sarahr", "contra000", "secretaria"))

    # def test_login_success(self):
    #     # Simula un inicio de sesión exitoso
    #     self.assertEqual(login("RaulAdm", "admin2345", "administrador"), "administrador")
    
    # def test_login_failure(self):
    #     # Simula un inicio de sesión fallido
    #     self.assertIsNone(login("Raul", "admin2345", "administrador"))

    def test_login_success(self):
        # Simula un inicio de sesión exitoso
        self.assertEqual(login("TavoGer", "gerent2578", "gerente"), "gerente")

    def test_login_failure(self):
        # Simula un inicio de sesión fallido
        self.assertIsNone(login("TavoGer", "contra000", "gerente"))


if __name__ == '__main__':
    unittest.main()
