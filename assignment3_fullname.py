firstname = ["aslam", "ali"]
lastname = ["ali", "khan"]

fullname = []
for i in firstname:
 for j in lastname:
  full_name = i + " " + j
  fullname.append(full_name)
print(fullname)
# fullname.remove("ali khan") 
# print(fullname)
del fullname[3]  # we can also do this using del function.
print(fullname)
