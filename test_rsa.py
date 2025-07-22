import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from base import RSA


class TestRsa(unittest.TestCase):
    def setUp(self):
        self.rsa = RSA()
        
    def test_encrypt_decrypt_ascii(self):
        message = "Descrete Math"
        ciphered = self.rsa.encrypt(message)
        decrypted = self.rsa.decrypt(ciphered)
        self.assertEqual(message, decrypted)
        
    def test_encrypt_decrypt_unicode(self):
        message = "سلام"
        ciphered = self.rsa.encrypt(message)
        decrypted = self.rsa.decrypt(ciphered)
        self.assertEqual(message, decrypted)
        
    def test_encrypt_decrypt_symbols(self):
        message = "@!"
        ciphered = self.rsa.encrypt(message)
        decrypted = self.rsa.decrypt(ciphered)
        self.assertEqual(message, decrypted)
        
        
    if __name__ == '__main__':
        unittest.main()