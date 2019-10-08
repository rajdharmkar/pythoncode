#for loop example and count letters in a word
#string = str(input("Enter any string:"))
string = raw_input("Enter any string:")
print len(string)
count = 0
for j in string:
    count +=1
    print j,
print "\n",count    
