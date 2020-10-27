import random

# Generate 1GB array

f = open("../demoGB.txt", "w")
for i in range(1, 210000000):
    f.write(str(random.randrange(1000, 9999)))
    f.write(",")
f.close()


# Generate 1MB array

f = open("../demoMB.txt", "w")
for i in range(1, 210000):
    f.write(str(random.randrange(1000, 9999)))
    f.write(",")
f.close()

