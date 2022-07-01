str1 = "Emma is a data scientist who knows Python. Emma works at google."
#Last occurrence of Emma starts at index 43
print(str1.count("Emma"))


#a useful method for this is to use rfind that returns a -1 if the string is not presented 
index = str1.rfind("Emma")
print(index)

str2 = "Emma-is-a-data-scientist" #split converts a string in a list with a separator 
print(str2.split("-"))
