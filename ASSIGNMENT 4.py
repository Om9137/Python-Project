#Task 1: Read a File and Handle Errors

file=open("Om.txt","w")
Write=file.write("Hello OM! Welcome to my home")
print(Write)
file.close()

file=open("Om.txt","r")
read=file.read()
print(read)
file.close()

file=open("Om.txt","r")
read=file.readline()
print(read)
file.close()

#Task 2: Write and Append Data to a File

file=open("Om.txt","w")
Write=file.readlines()
print(Write)
file.close()

file=open("Om.txt","a")
append=file.write(input("Write the page:"))
print(append)
file.close()
