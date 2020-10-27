f = open("../demoGB.txt", "r")
string_array = f.read()
f.close()
array = []


rows = string_array.split(",")
for i in range(0, len(rows)):
    array += [int(rows[i])]

array.sort(reverse=True)
take_n = array[:125000]
print(take_n)
