# Program to disply ASCII code of all character in a string

print("Please enter the String: ", end="")
string = input()


def ascii(string):
    string_length = len(string)


for K in string:
    ASCII = ord(K)
    print(K, "\t", ASCII)
