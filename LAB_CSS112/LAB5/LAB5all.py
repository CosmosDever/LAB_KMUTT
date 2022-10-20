#1
try:
    File= open("myFile.txt","r")
    print(File.read())
    print('Successfully print content in myFile.txt')
except :
    print("Unable to open file myFile.txt")
#2
File= open("myFile.txt","r")
print(len(File.read()))
#3
File= open("myFile.txt","r")
num=File.read().split()
print(len(num))
