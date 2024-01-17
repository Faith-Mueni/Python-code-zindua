# a dictionary is a data structure that allows you to store data in a key value format
# a dictionary is created using curly braces {} and the key-value pairs are separated by a comma

results = {
   "Jane": 40,
   "Brian": 34,
   "Jack":70
}

#print(results["Jack"])

#results ["John"] = 80 #assigning a new value that was not in the dictionary

#print(results.get("John")) # using .get is an alternative for pulling the result

print (results.keys()) # it will give all the values in the curly brackets

new_results = {
    "Jade": "Invalid",
    "kenndedy": "incomplete"
}

results.update (new_results) # assigning more values to the previous values

#coding chalenge: write a simple python program to update the value of a key in the results dictionary

new_results [ "kennedy"] = "valid"

print(new_results)

if "Jade" in results:
    print ("Jade did the test!")
else:
    print("Either Jade did not do the test or isn't a student!")

print(results.items()) # it LISTS all the values in the dictionary

family = {
    "grandparents": {
        "grandfather": "John Doe",
        "grandmother": "Jane Doe",
        "children ": {
            "firstborn": "Jack Doe",
            "lastborn": "June Doe"
           }
        },
        "cousins": ["Jake","Jude","John"]
    }
