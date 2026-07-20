def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def rsa_encrypt(m, e, n):
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    return pow(c, d, n)

# Test Case 1
p, q, e, m = 3, 11, 3, 4
n = p * q
phi = (p-1) * (q-1)
d = mod_inverse(e, phi)
c = rsa_encrypt(m, e, n)
recovered = rsa_decrypt(c, d, n)

print("RSA Test Case 1:")
print(f"n = {n}, phi = {phi}, e = {e}, d = {d}")
print(f"Encrypted: {c}, Decrypted: {recovered} (Original: {m})")

# Test Case 2 (your choice)
p2, q2, e2, m2 = 5, 7, 5, 12
n2 = p2 * q2
phi2 = (p2-1) * (q2-1)
d2 = mod_inverse(e2, phi2)
c2 = rsa_encrypt(m2, e2, n2)
recovered2 = rsa_decrypt(c2, d2, n2)

print("\nRSA Test Case 2:")
print(f"n = {n2}, phi = {phi2}, e = {e2}, d = {d2}")
print(f"Encrypted: {c2}, Decrypted: {recovered2} (Original: {m2})")
