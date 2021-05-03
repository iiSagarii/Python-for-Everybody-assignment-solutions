s1 = '/Users/Sagar Pujari/PycharmProjects/'
s2 = '.txt'
user = input("Enter the file name : ")
file = open(s1+user+s2,'r',encoding='utf-8')

list1 = list()
for lines in file :
    if lines.startswith("From ") :
        name = lines.split()
        nm = (name[1])
        n= nm.split("@")
        list1.append(n[0])
        #print(list1)

dict1 = dict()
for count in list1:
    dict1[count] = dict1.get(count,0) + 1
print(dict1)
