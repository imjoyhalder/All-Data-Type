child1 = {"name":"Joy",
        "Age": 18,
        "Class": 11,
        "Department": "CST"}

child2 = {"name":"Arijit",
        "Age": 19,
        "Class": 11,
        "Department": "EEE"}

child3 = {"name":"Debojit",
        "Age": 17,
        "Class": 11,
        "Department": "Science"}

child4 = {"name":"Nondon",
        "Age": 15,
        "Class": 12,
        "Department": "CT"}

child5 = {"name":"Sujoy",
        "Age": 20,
        "Class": 12,

        "Department": "Arts"}
Child = {"Child1":child1,
        "Child2": child2,
        "Child3": child3,
        "Child4": child4,
        "Child5": child5}
print(Child)
for i in Child.items():
    print(i)
print(Child["Child4"])