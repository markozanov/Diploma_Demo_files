f = open("../demoGB.txt", "r")


results = []

AVG = 0
SUM = 0
COUNTER = 0
x = 0
while True:
    line = f.read(10)
    if line == "":
        break
    numbers = line.split(",")
    x += 1
    print(str(numbers) + " " + str(x))

    SUM += int(numbers[0]) + int(numbers[1])
    COUNTER += 2
    AVG = (AVG + SUM) / COUNTER


f.close()
w = open("../demoGBLSResult.txt", "w")
for i in range(0, 210000):
    w.write(str(AVG))
    w.write(",")
w.close()
