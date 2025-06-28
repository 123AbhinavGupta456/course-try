# Write prime numbers up to a given limit

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

limit = 100  # Change this value as needed
for num in range(2, limit + 1):
    if is_prime(num):
        print(num)