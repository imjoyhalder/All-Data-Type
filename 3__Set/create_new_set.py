set1 = {"Meghla","Biswas","computer","Science","BPI","4th","Meghla","Meghla","Meghla"}
#print("\n")
#print(set1)

# find out the lenght of set1
#print(len(set1))

# set convert in list (this is called type casting)
lsit1 = list(set1)
#print(lsit1)

# list convet in tuple (this is also called type casting)
list2  = tuple(set1)
#print(list2)


# range prameter
# range(start , end, steps)
#        1    , 100, 2

# for loop use into a set

counter = 0
for i in set1:
    #print(i)
    counter +=1
    if ("BPI" in set1):
        #print(True)
        break
#print(counter)
        
#a = int(input("Enter the value of a:"))
#b = int(input("Enter the value of b:"))

# ternary operator   condition ? return expression1 : return expression2

#print("a is the largest number") if (a>b) else print("b is the largest number ")


# add()
name = {"meghla","toun","bristy","anuska","Dipika","Rasmika"}
name.add("Dristry")
#print(name)

institue = {"BPI","CPI","DPI","LPI","KPI","NPI"}
#name.update(institue)
#print(name)

institue.update(name)
#print(institue)

# sorted() method convert a set into the list
#print(sorted(institue))


wait_list = ["50kg","45kg","34kg","56kg","60kg"]
year_list ={19,18,17,13,14}

year_list.update(wait_list)
#print(year_list)

wait_list.extend(year_list)
#print(wait_list)

new_set = set(wait_list)
#print(new_set)


#remove()
try:
    new_set.remove("100kg")
except KeyError:
    #print("There have no element like this")
    pass
finally:
    #print(new_set)
    pass

#discard()
new_set.discard("60kg")
#print(new_set)
    
#pop()
new_set.pop()
#print(new_set)

#clear()
new_set.clear()
#print(new_set)

# del
#del new_set
#print(new_set)

a = new_set.union(year_list)
#print(a)

#difference()
s1 = {"google","apple","bubble","sort"}
s2  = {"apple","joker","bubble","index"}
#a = s1.difference(s2)
#print(a)

b = s2.difference(s1)
#print(b)

c = s1.difference_update(s2)
print(c)