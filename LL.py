f = open("../demoGB.txt", "r")
w = open("../demoGBLLResult.txt", "w")

results = []

x = 0
while True:
    line = f.read(10)
    if line == "":
        break
    numbers = line.split(",")
    x += 1
    print(str(numbers) + " " + str(x))
    SUM = int(numbers[0]) + int(numbers[1])
    AVG = SUM/2
    w.write(str(SUM) + "," + str(AVG))

f.close()
w.close()
