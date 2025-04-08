#opening files
file = open("example.txt", "r") #opens file in read mode
data = file.read()

#reading files
with open("example.txt", "r") as file: data = file.read() 
print(data)
#processing large  datasets or analyzing text documents

#writing and appending to files
with open("output.txt", "w") as file: file.write("Hello,python!")


#closing files
#use with statement
