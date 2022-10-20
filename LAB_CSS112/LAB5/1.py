
try:
    File= open("myFile.txt","r")
    print(File.read())
    print('Successfully print content in myFile.txt')
except :
    print("Unable to open file myFile.txt")
