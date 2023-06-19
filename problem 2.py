# Calculate the even-valued solutions of the Fibonacci Sequence below 4 million

a, b = 1, 2
total = 0

while total < 4000000:
    c = a + b
    a, b = b, c
    if c % 2 == 0:
        total += c

print(total + 2)
