car = {
  "brand": ["Hero","Marcedis","Honda","Apache","Palsure","Suzuki"],
  "model": ["MT50","20T","Zn10","LI12","00R","T3Np"],
  "year": 1964,
  "Semester": ["1st","2nd","3rd","4th","5th","6th","7th"]
}

#print(car,"\n")

# items()
e = car.items()
#print(e)

# keys()
f = car.keys()
#print(list(f))


#fromkeys()
c = car.fromkeys(car,"All")
print(c)
#print('')


# get()
d = car.get("model"[3])
#print(d)

##copy
#b = car.copy()
#print(b)
#print(" ")
#
## Clear 
#a = car.clear()
#