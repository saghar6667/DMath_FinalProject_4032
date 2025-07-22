import random

class RSA:
    def __init__6(self):
        self.e = 65537
        self.p, self.q, self.n, self.phi_n = self._choose_primes()
        self.d = self._mod_inverse(self.e, self.phi_n)

    def _is_prime(self, number):
        if number < 2:
            return False
        if number == 2:
            return True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def _generate_prime(self):
        candidates = list(range(10**5, 10**6))
        random.shuffle(candidates)
        for num in candidates:
            if self._is_prime(num):
                return num
        raise ValueError("No prime number found in range")
    
    def _gcd(self, a, b):
        while b:
            a,b = b, a % b
        return a
    
    def _choose_primes(self):
        while True:
            p = self._generate_prime()
            q = self._generate_prime()
            if p != q:
                n = p * q
                phi_n = self.computePhi(p,q)
                gcd = self._gcd(self.e, phi_n)
                if gcd == 1:
                    return p, q, n, phi_n

    def _mod_inverse(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            a, m = m, a % m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1
    
    def computePhi(self, p, q):
        return (p - 1) * (q - 1)
    
    def _split_into_blocks(self, message, block_size):
        return [message[i:i + block_size] for i in range(0, len(message), block_size)] 

    def encrypt(self, message):
        message_bytes = message.encode("utf-8")
        max_block_size = (self.n.bit_length() - 1) // 8
        blocks = self._split_into_blocks(message_bytes, max_block_size)
        encrypted_blocks = [pow(int.from_bytes(block, 'big'), self.e, self.n) for block  in blocks]
        return ' '.join(hex(b)[2:] for b in encrypted_blocks)

    def decrypt(self, ciphertext):
        encrypted_blocks = [int(block, 16) for block in ciphertext.split()]
        decrypted_bytes = b''.join(pow(block, self.d, self.n).to_bytes((block.bit_length() + 7)
                                    // 8, 'big')for block in encrypted_blocks)

        return decrypted_bytes.decode('utf-8')
    
    def get_public_key(self):
        return (self.e, self.n)

    def get_private_key(self):
        return (self.d, self.n)