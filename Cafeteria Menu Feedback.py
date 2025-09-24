# Example: Working with Integers in Python

# Declare integer variables
Qt1 =10
Qt2 = 5
Qt3 =6
Qt4 =9
# Basic arithmetic operations
sum_result = Qt1 + Qt2
Average_result = (Qt1 + Qt2 + Qt3 + Qt4) / 4
minimum_result = (min(Qt1, Qt2, Qt3, Qt4))
maximum_result = (max(Qt1, Qt2, Qt3, Qt4))
print("Sum:", sum_result)#output=30
print("Average:", Average_result)#output=7.5
print("Minimum:", minimum_result) # output=5
print("Maximum:", maximum_result)  # output=10
#strings
report="The sum is " + str(sum_result) + ", the average is " + str(Average_result) + ", the minimum is " + str(minimum_result)
report2 = "5, and the maximum is " + str(maximum_result) + "."# output= sum_result(30),Average_result(7.5),maximum_result(10),minimum_resul(5)
#booleans
threshold = 7
is_above_threshold = Average_result > threshold
if Average_result > threshold:
    print("above standard")
else:
    print("below standard")
    #lists
menu_items = ["rice", "beans", "fish"]
print("original list:", menu_items)
menu_items.append("chicken")#output=orginal list:["rice", "beans", "fish","chicken"]
menu_items.remove("beans")
menu_items.sort()
print("updated list:", menu_items) #output=original list:['chicken', 'fish', 'rice']
#arrays
import array as arr
quantities = arr.array('i', [Qt1, Qt2, Qt3, Qt4])
print("original array:", quantities)
#dictionaries
# menu_items = {"rice": Qt1, "beans": Qt2, "fish": Qt3}
print("orginal dictionary:", menu_items)
menu_items[1] = "Peas"
del menu_items[2]
print("updated dictionary:", menu_items) #output=original dictionary: ['rice', 'fish', 'chicken']



