#file = open("words.txt","r")
#print (file.read()) #to get the whole content

#contents = file.read() # alternative 2

with open ("words.txt","r") as file:
    contents = file.readline()

    print(contents)

""" 
"r" : opens a file in read mode
"w" : opens a file in write mode
"a" : opens a file in append mode
"""

lines = [
    "statistics",
 "you got this!"
]

with open("examplefile.txt","a") as file:
    file.writelines(lines)

with open ("words.txt","r") as file:
        for line in file:
            print(line)


