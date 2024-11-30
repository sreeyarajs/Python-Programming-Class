list1=[1,2,3,4]

filePath = "data.txt"

with open(filePath,"w") as fileHandle:
    fileHandle.write(str(list1))

with open(filePath,"r") as fileHandle:
    readData = fileHandle.read()
    readData = readData[1:len(readData)-1].replace("","").split(",")
    print(f"read data is {readData} \n its type is{type(readData)}")