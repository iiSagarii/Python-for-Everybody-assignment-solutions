# Open the file mbox-short.txt and read it line by line. 
# When you find a line that starts with 'From' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). 
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.

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
