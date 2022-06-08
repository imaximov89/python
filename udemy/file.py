# file = open('test.txt')

# print(file.read())

# file.close()

with open("C:\\Users\\Игорь\\Documents\\DevOps\\python\\test.txt", mode='r+') as myfile:
    print(myfile.read())
