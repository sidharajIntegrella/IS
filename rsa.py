class RSA:
    # selecting two prime numbers p and q
    def __init__(self,p=17,q=23):
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        
        # choose a public key such that 0 < e < phi and gcd(e,phi)=1
        self.public_key = 5

        self.private_key = self._find_private_key(self.phi)
    
    def _find_private_key(self, phi):
        for d in range(1, phi):
            if (d * self.public_key) % phi == 1:
                return d
        return None
    
    def modPow(self,base, exp, mod):
        result = 1
        base = base % mod
        
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp = exp // 2
        
        return result
    
    def encrypt(self, plaintext):
        # ciphertext = (plaintext ^ e) mod n
        return self.modPow(plaintext, self.public_key, self.n)

    def decrypt(self, ciphertext):
        # plaintext = (ciphertext ^ d) mod n
        return self.modPow(ciphertext, self.private_key, self.n)
    
    def to_string(self):
        return f"p: {self.p}, q: {self.q}, n: {self.n}, phi: {self.phi}, public_key: {self.public_key}, private_key: {self.private_key}"

rsa = RSA()

print(rsa.to_string())

msg = 12

enc = rsa.encrypt(msg)

print("Original:", msg)
print("Encrypted:", enc)
print("Decrypted:", rsa.decrypt(enc))