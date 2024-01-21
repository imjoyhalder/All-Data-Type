student = {
    "Name": ["Meghla","Mim","Chumki","Liza","Papri","Tonu"],
    "Dempartment" : ["CST","ET","MT","CT",'PWT','EET'],
    "Semester" : ["1st","2nd","3rd","4th","5th","6th","7th"],
    "Roll" : [1,2,3,4,5,6,7]
}

# get()
info_get = student.get("Semester")
#print(info_get)

#fromkeys()
set_value = student.fromkeys(student,"All")
#print(set_value)

#items()
get_item = student.items()
#print(get_item)

#keys()
get_all_keys = student.keys()
#print(get_all_keys)

#pop()
delete_item = student.pop("Name")
#print(student)

#popitem()
student.popitem()
print(student)