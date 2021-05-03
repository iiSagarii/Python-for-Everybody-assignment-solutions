file = open('/Users/Sagar Pujari/PycharmProjects/textfile.txt','r',encoding="utf-8")
for line in file :
    line=line.strip()
    print(line.upper())