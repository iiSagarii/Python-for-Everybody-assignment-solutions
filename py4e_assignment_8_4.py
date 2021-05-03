# Open the file textfile.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.


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
