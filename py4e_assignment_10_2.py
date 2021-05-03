# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.

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
