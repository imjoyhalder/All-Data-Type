car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# items
e = car.items()
print(e)

# keys
f = car.keys()
print(f)

#fromkeys
c = car.fromkeys(car,0)
print(c)
print('')

# get
d = car.get("brand")
print(d)

#copy
b = car.copy()
print(b)
print(" ")

# Clear 
a = car.clear()
