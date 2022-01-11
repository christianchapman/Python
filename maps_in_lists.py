
#!/usr/bin/python


nam1 = "firstint"
nam2 = "secondint"
val1 = "desc 10.1.1.1"
val2 = "desc 10.2.2.2"

list_of_keys=[]
list_of_keys.append({ nam1 : val1})
nam1 =  "secondint"
val2 = "desc 20.2.2.2"
list_of_keys.append({ nam1 : val2})
for k in list_of_keys :
    print ("interfaces are %20s\n" % (k.keys()) )
    print ("descriptions are %20s\n" % (k.values()) )

## print a certain value

print ("This is the value of one of the interfaces %-20s" % (list_of_keys[0]["firstint"]))


a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}



print ("\n\nprint all items\n\n")
for i in a_dict.items() :
      print i


print ("\n\nprint keys\n\n")

for j in a_dict :
    print j

print ("\n\nprint values\n\n")

for k in a_dict.values() :
     print k

# To get a specific value

print ("This is the value %-20s" % (a_dict["color"]))
