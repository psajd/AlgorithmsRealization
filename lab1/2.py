fin = open("aplusbb.in")
fout = open("aplusbb.out", "w")
a, b = map(int, fin.readline().split())
c = int(a + b*b)
print(c, file=fout)
