# Integers 1 - 10

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

print("This is a set of odd numbers:", odds)
print("This is a set of even numbers:", evens)
print("This is a set of prime numbers:", primes)
# Integers which can be factored
print("This is a set of composite numbers:", composites, "\n")

print("This is the union of odds with evens:")
print(odds.union(evens), "\n")

print("The union of evens with odds is the same:")
print(evens.union(odds), "\n")

print("Show the set of odd numbers which are also prime numbers using intersection:")
print(odds.intersection(primes), "\n")

print("Or show the set of even numbers which are prime using intersection:")
print(evens.intersection(primes), "\n")

# Check if 2 is in the set of prime numbers
n = 7
print("Is", n, "in the set of prime numbers prime number?", n in primes)
