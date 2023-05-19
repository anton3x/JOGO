a = open("asdas.txt", "w")
a.write("global ")
for i in range(16):
    a.write("posx" + str(i + 1) + " ,")
    a.write("posy" + str(i + 1) + " ,")
    a.write("posx" + str(i + 1) + "_1 ,")
    a.write("posy" + str(i + 1) + "_1 ,")