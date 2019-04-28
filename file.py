"""
	Program to experiment file operations using python.
"""
import celToFar

celToFar.create()

fil = open('exampleText','r')
content = fil.readlines()
fil.close()
content = [ i.rstrip('\n') for i in content]
for i in content:
    print(len(i))
line = ['line1','line2','line3','line4','line787']
newFile = open("temp3",'w+')
for no in line:
    newFile.write(no+'\n')
print(newFile)
newFile.close()
