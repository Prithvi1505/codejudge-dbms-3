def mod_pow(base, exp, mod):
    return pow(base, exp, mod)

# Test Case 1 (given)
p, alpha, a, b = 29, 2, 5, 12
A = mod_pow(alpha, a, p)
B = mod_pow(alpha, b, p)
K_alice = mod_pow(B, a, p)
K_bob = mod_pow(A, b, p)

print("Diffie-Hellman Test Case 1:")
print(f"A = {A}, B = {B}")
print(f"Shared Key (Alice): {K_alice}, (Bob): {K_bob} → Match: {K_alice == K_bob}")

# Test Case 2
p2, alpha2, a2, b2 = 23, 5, 6, 15
A2 = mod_pow(alpha2, a2, p2)
B2 = mod_pow(alpha2, b2, p2)
K_alice2 = mod_pow(B2, a2, p2)
K_bob2 = mod_pow(A2, b2, p2)

print("\nDiffie-Hellman Test Case 2:")
print(f"A = {A2}, B = {B2}")
print(f"Shared Key (Alice): {K_alice2}, (Bob): {K_bob2} → Match: {K_alice2 == K_bob2}")
