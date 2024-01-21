# create a list
 #   index 0     1      2    3     4
list1 = ["BPI","DPI","CPI","LPI","KPI"]
#negative -5    -4    -3     -2   -1
#print(list1[:4]) 
#print(list1[-2: ])
#print(list1[-1: -5 ])


# append()
list1.append("jpi")
#print(list1)

#count()
#print(list1.count("LPI"))

# extend()
list2 = ["Meghla","Biswas","computer"]
#list1.extend(list2)
#print(list1)


list3 = ["Meghla","Biswas","computer",["1st","2nd","3rd","4th",'5th']]
#print(list3[3][3])


#copy()
x = list3.copy()
#print(x)

# data inserting in simple way
list3[3] = "6th"
#print(list3)
#

# insert()
list3.insert(1,"CST")
#print(list3)


# pop()
list3.pop()
#print(list3)


# remove
list3.remove("Biswas")
#print(list3)


#reverse()

list3.reverse()
#print(list3)

#sort()
list4 = [6,3,2,0,-2,4,-12,-5]
print("This is a sorted list")
list4.sort()
print(list4)

print("\nThis is a reversed list")
list4.sort(reverse=True)
print(list4)
