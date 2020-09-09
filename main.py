n = int(input("Enter the number of lines for the Bell's triangle: "))

bell = [[1]]

for j in range(1, n):
    new_line = []
    new_line.append(bell[j - 1][-1])
    for k in range(len(bell[j - 1])):
        new_line.append(bell[j - 1][k] + new_line[k])
    bell.append(new_line)

for i in bell:
    print(*i, sep=" ")
