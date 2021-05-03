s1 = '/Users/Sagar Pujari/PycharmProjects/'
s2 = '.txt'
user = input("Enter the file name : ")

try:
    file = open(s1+user+s2,'r',encoding="utf-8")
except:
    print("file dosent exits")
    quit()

lst = list()
for line in file:
    if line.startswith("From "):
        word = line.split()
        time = word[5]
        hours = time.split(":")
        lst.append(hours[0])
        #print(hours)

dt = dict()
for h in lst:
    dt[h] = dt.get(h,0) + 1
#print(dt)

for k,v in sorted(dt.items()): # sorted is used to sort the dict in ascending order
    print(k,v)