#exception handling,try-except

try:
    file = open("example.txt", "r")
    data = file.read()

    print(data)
except FileNotFoundError:
    print("Sorry!File does not exist")
finally:
    print("Thank you for using this program")
