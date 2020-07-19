f = open("chat.txt", "r")
fw= open("chatdata2.txt", "wr")
for i in range(10000):
    a=str(f.readline())
    if i>112:
        a=str(f.readline())
        b=a.split("  ")
        b=b[0].split("\t")
        b=b[:-2]
        fw.write('{"tag": "chat'+str(i)+'",\n')
        fw.write('"patterns": ["'+b[0]+'"],\n')
        fw.write('"responses": ["'+b[1]+'"],\n')
        fw.write('"context_set": ""\n')
        fw.write(' },\n')

fw.close()

