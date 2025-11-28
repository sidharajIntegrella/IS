# Requires 2048–4096-bit primes
# 2 users a and b

# is public
prime = 23
# is public
generator = 5

# alice
secret_a = 6 # 1 ≤ secret_a < p randomly chosen

public_a = (generator ** secret_a) % prime # gen ^ secret_a mod prime

# bob
secret_b = 15 # 1 ≤ secret_b < p randomly chosen
public_b = (generator ** secret_b) % prime # gen ^ secret_b mod prime

# public values: generator, prime, public_a, public_b

def generate_shared_secret(public_key, secret):
    return (public_key** secret) % prime

# used by bob
shared_secret_a = generate_shared_secret(public_b, secret_a)

# used by alice
shared_secret_b = generate_shared_secret(public_a, secret_b)

print("User A Public Key:", public_a)
print("User B Public Key:", public_b)
print("Shared Secret from A:", shared_secret_a)
print("Shared Secret from B:", shared_secret_b)