user = input("Enter file name : ")
s1 = "/Users/Sagar Pujari/PycharmProjects/"
s2 = ".txt"
list1 = list()
try:
    file = open(s1+user+s2,'r',encoding="utf-8")
except:
    print("file dosent exits")
    quit()
for line in file:
    if line.startswith('From'):
        words = line.split()
        print(words[1])