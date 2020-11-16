def fibonacci(n):
    fib_array = [1, 1]

    while True:
        x = fib_array[-2] + fib_array[-1]
        if x > n:
            break
        fib_array += [x]

    return fib_array


f = open("../demoMB.txt", "r")
string_array = f.read()
f.close()
array = []

rows = string_array.split(",")
for i in range(0, len(rows)):
    array.append(int(rows[i]))


fibonacci_of_all_elements = []

for i in range(0, len(array)):
    fibonacci_of_all_elements += [fibonacci(array[i])]

# print(fibonacci_of_all_elements)
f = open("../fibonacci.txt", "w")
for i in range(0, 60):
    f.write(str(fibonacci_of_all_elements))
f.close()




