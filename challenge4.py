"""
Write a Python program that analyzes a text file and performs the following tasks:
Ask the user to enter the name of a text file to analyze.
Open the file and read its contents.
Count the number of lines in the file and print it.
Count the number of words in the file and print it.
Count the number of characters (including whitespace) in the file and print it.
Determine the average word length in the file and print it.
Determine the most common word in the file and print it.
Create a new file called "analysis.txt" and write the analysis results to it in the following format:Number of lines: [count]
Number of words: [count]
Number of characters: [count]
Average word length: [average]
Most common word: [word]
Make sure to handle any exceptions that may occur, such as when the file does not exist or cannot be opened.
You can use any relevant Python concepts covered in the lesson, such as file input/output, string
"""

file = open ("words.txt", "r")
#print (file.read())

count = 0
for line in file:
    count = count + 1
print ("line count:", count)

def get_some_letters (word):
    letters = []

    for char in list (word):
        if char not in letters:
            letters.append(char)



