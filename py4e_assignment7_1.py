# write a program that prompts for a file name, then opens that file and reads through the file,
# Use the file words.txt to oproduce the output below

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
