import re
"""
\d: mathches any digit (0-9)
\w: matches any word character (a-z, A-Z, 0-9 and _)
\s : matches any whitespace characters (space, tab, newline)
[]: any characters inside the square brackets
( ): Matches any characters inside the square brackets
"""
#pattern = re.compile ("Hello (\w+)") 

#result = pattern.search ("Hello Python")

#print (result)


#pattern = r"\d{3}-\d{3}-\d{3}"

#text = "apple. I'm not a doctor!, 245-341-678"

#result = re.search (pattern, text)

#if result:
    #print ("match found", result.group())
#else:
    #print ("not found")

"""
write a regular expression pattern for the following phone Number 254 797321801
"""
pattern = r"\d{3}\s\d{9}"

text = "254 797321801"

result = re.search (pattern,text)

if result:
    print ("match found", result.group())

else:
    print ("not found")