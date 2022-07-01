str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
str2=[]
for i in str_list:
    if i == None or i == "":
        continue
    str2.append(i)
print(str2)