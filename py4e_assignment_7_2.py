user = input("Enter file name : ")
s1 = "/Users/Sagar Pujari/PycharmProjects/"
s2 = ".txt"
count = 0
file = open(s1+user+s2,'r',encoding="utf-8")
for line in file :
    words = line.split()
    for word in words:
        if word == 'program':
            count = count + 1
            word = "programmer"
    print(line)
print("program is present",count,"times")
file.close()
#file = open(s1+user+s2,'r',encoding="utf-8")
#for lines in file :
 #   lines = lines.replace("program","programmers")
  #  lines = lines.strip()
   # print(lines)
#file.close()

