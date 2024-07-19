firstname = ["aslam", "ali"]
lastname = ["ali", "khan"]

fullname = []
for i in firstname:
 for j in lastname:
  x = firstname.index(i)
  y = lastname.index(j)
  if (x == y):
   fullname.append(i + " " + j)
  else:
   continue
print(fullname)
