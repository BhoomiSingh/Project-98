def swapFileData():
    print("Swap File")

    print("Name of files to be swapped:-")

    firstFile = input("Enter the name of first file: ")
    secondFile = input("Enter the name of second file: ")

    with open(firstFile, 'r') as a:
        dataA = a.read()

    with open(secondFile, 'r') as b:
        dataB = b.read()

    with open(firstFile, 'w') as a:
        a.write(dataB)

    with open(secondFile, 'w') as b:
        b.write(dataA)

    print("The data has been swapped")

swapFileData()
