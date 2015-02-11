def is_lower_case(value):
    if value.lower() == value:
        return True


print('This program currently only works with 16x16 Punnett Squares.')
print()
p1 = input('Enter the genotype of the first parent:')
p2 = input('Enter the genotype of the second parent:')
print()

if not p1.lower() == p2.lower():
    print('Those genotypes are not valid!')
    exit()

if not p1.__len__() == 8:
    print('Those genotypes are not valid!')
    exit()

for i in range(0, 4):
    if not p1[(i * 2) - 1].lower() == p1[(i * 2) - 2].lower():
        print('Those genotypes are not valid!')
        exit()

numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

for i in range(0, 10):
    if p1.__contains__(numbers[i]):
        print('Those genotypes are not valid!')
        exit()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numberOfLetters = 26

for i in range(0, 4):
    stop = True
    for j in range(0, numberOfLetters):
        if p1[(i * 2) - 7].lower() == letters[j]:
            stop = False

    if stop:
        print('Those genotypes are not valid!')
        exit()
    else:
        letters.remove(p1[i * 2].lower())
        numberOfLetters -= 1

pattern = (
    "1111", "1112", "1121", "1122", "1211", "1212", "1221", "1222", "2111", "2112", "2121",
    "2122", "2211", "2212", "2221", "2222")

pl1 = []
pl2 = []

for i in range(0, 4):
    pl1.append(p1[(i * 2) - 7] + p1[(i * 2) - 8])
    pl2.append(p2[(i * 2) - 7] + p2[(i * 2) - 8])

pl3 = []
pl4 = []

for i in range(0, 16):
    i1 = int(pattern[i][0]) - 1
    i2 = int(pattern[i][1]) - 1
    i3 = int(pattern[i][2]) - 1
    i4 = int(pattern[i][3]) - 1
    pl3.append(pl1[0][i1] + pl1[1][i2] + pl1[2][i3] + pl1[3][i4])
    pl4.append(pl2[0][i1] + pl2[1][i2] + pl2[2][i3] + pl2[3][i4])

pl5 = []

for i in range(0, 16):
    for j in range(0, 16):
        pl5.append(pl3[i] + pl4[j])

for i in range(0, 256):
    s = pl5[i]
    s1 = s[0] + s[4]
    s2 = s[1] + s[5]
    s3 = s[2] + s[6]
    s4 = s[3] + s[7]
    pl5[i] = s1 + s2 + s3 + s4
    s = pl5[i]
    l1 = []
    for j in range(0, 4):
        s1 = pl5[i][j * 2] + pl5[i][j * 2 + 1]
        if is_lower_case(s1[0]):
            s2 = s1[1]
            s3 = s1[0]
            s1 = s2 + s3
        l1.append(s1)
    pl5[i] = l1[0] + l1[1] + l1[2] + l1[3]

l1 = []
d1 = {}
j = 0

for i in range(0, 256):
    if not l1.__contains__(pl5[i]):
        l1.append(pl5[i])
        d1[pl5[i]] = j
        j += 1

l2 = []

for i in range(l1.__len__()):
    l2.append(0)

for i in range(0, 256):
    l2[d1[pl5[i]]] += 1

print("There are a total of " + str(l2.__len__()) + " distinct genotypes.")
print("Possible genotypes of the offspring of the two parents:")
print()
for i in range(0, l1.__len__()):
    print(l1[-i - 1] + ": " + str(l2[i]))