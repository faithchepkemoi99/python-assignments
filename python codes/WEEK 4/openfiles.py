#read file
file = open("example.txt", "r")
data = file.read()

print(data)

#write mode
file = open("randomfile.pdf", "w")
data = file.write("Amazing work here!")

print(data)