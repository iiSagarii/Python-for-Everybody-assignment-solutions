user = input("Enter the file name:")
s1 = '/Users/Sagar Pujari/PycharmProjects/'
try :
    file = open(s1+user,'r',encoding="utf-8")
except:
    print("file dosent exits")
    quit()
for line in file:
    line = line.rstrip()
    print(line)