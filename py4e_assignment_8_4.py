file = open('/Users/Sagar Pujari/PycharmProjects/textfile.txt','r',encoding="utf-8")
list1 = list()
for line in file:
    words = line.split()
    for word in words :
        if word in list1 :
            continue
        else:
            list1.append(word)
list1.sort()
print(list1)
