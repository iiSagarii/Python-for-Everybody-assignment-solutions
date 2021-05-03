# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

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
