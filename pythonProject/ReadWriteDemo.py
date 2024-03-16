#test file - abc bdv cedf dhjk elephant
#Open(pass the full path with file extension)
#same project path just pass the file name with extension
#Step 1 open the file # create a object
file  = open('test.txt')

#Step 2 Read all content in the file file.read()
#print(file.read())

#Note:once read control will be in that character position
#To Read first 2 characters in the file
#print(file.read(2)) #a + b= output is ab
#print(file.read(5)) # a + b + c + newline + e = so total 5 characters abc e will be the output

#now control is in secondine e===>dv
#Readline ->read one single line at a time
#print(file.readline()) # dv
#print(file.readline()) #cedf

#Interview Ques - print line by line using readline method

#line = file.readline()
#while line!="":
 #   print(line)
  #  line = file.readline()

#Readlines - each and evey lines stored in a list like example
#index 0 = abc , index 1=edv, index 2=cedf, index 4=dhjk, index 5=elephant
#print(file.readlines()) #['abc\n', 'edv\n', 'cedf\n', 'dhjk\n', 'elephant']
#Advantage of having these values as a list it iseasy to iterate extract the values from the list
#How to iterate and print from the list, here this line object will pull one value from the list for each iteration
for line in file.readlines():
    print(line)

#Close the File
file.close()