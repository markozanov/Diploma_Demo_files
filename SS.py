import sys
f = open("../demoMB.txt", "r")
string_array = f.read()
f.close()
array_to_sort = []


rows = string_array.split(",")
for i in range(0, len(rows)):
    array_to_sort.append(int(rows[i]))

print(array_to_sort)

array_sorted = array_to_sort
array_sorted.sort(reverse=True)

f = open("../sorteddemoMB.txt", "w")
for i in range(0, len(array_sorted)):
    f.write(str(array_sorted[i]))
    f.write(",")
f.close()
