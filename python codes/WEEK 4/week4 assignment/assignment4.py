
#read file contents
file = open("input.txt", "r")
data = file.read()
print(data)

#count number of words
words = data.split()
word_count = len(words)
print(word_count)

#convert all to uppercase
uppercase_data = data.upper()
print(uppercase_data)


#processed text and the word count to a new file called output.txt.
file = open("output.txt", "w")
file.write(uppercase_data)
file.write("word_count:39")
file.close()


try:
    file = open("output.txt", "r")
    data = file.read()

    print(data)
except FileNotFoundError:
    print("Sorry!File does not exist")
finally:
    print("Thank you for using this program")

