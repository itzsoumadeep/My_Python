#WRITING A FILE
''' Writing data to the file :
f.write(str)--> A single string in there
f.writelines(list of lines)-->If we write a group of string present in list or touple
'''
f=open ('abc.txt','w')
f.write("Soumadeep ")
f.write("Ghosh")
f.write(" roll:33200121071\n")
f.write("College:TIB\n")
f.close()
print("Write operation is complited")

f=open('sd.txt','w')
l=['Bubay\n','Soumadeep\n','Ghosh\n','SD\n']
f.writelines(l)
f.close()
print("Write operation is complited")

fname=input("Enter file name: ")
f=open('E:\\Input\\'+fname,'w')#--> Creat file from user and enter data dynamically......
l=input("Enter data")
f.writelines(l)

f.close()
'''Reading  character data from the text files:
    ------------------------------------------
f.read()==> To read total data from the file
f.read(n)==> To read n  character from the file
f.readline()==>to read only one line
f.readlines()==>To read all lines into a list'''


f=open ('abc.txt','r')
data=f.read()
print(data)
line=f.readline()
print(line)

f=open('abc.txt')
lines=f.readlines()
for line in lines:
    print(lines,end=' ')
#copy data one file to another

f1=open('abc.txt')
f2=open('output.txt','w')
f2.write(f1.read())
f1.close()
f2.close()
print('data copy abc.txt to output.txt')

# to close the file automatically
with open('abc.txt','w') as f:
    f.write("Fuckkk ")
    f.write("Offff")
    f.write("!!!!!!!!!!!!")
    print('if file closer???? ',f.closed)
print('if file closer???? ',f.closed)







