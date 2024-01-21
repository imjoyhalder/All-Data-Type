Child = {"child1":{"name":"Adi",
        "class":1,
        "age":6,
        "Roll":2,
        "Hight":"3 fit"},

        "child2":{"name":"Rodin",
        "class":3,
        "age":7,
        "Roll":20,
        "Hight":"3.5 fit"},

        "child3":{"name":"Ashik",
        "class":5,
        "age":10,
        "Roll":4,
        "Hight":"4.8 fit"}
}
for i in Child.items():
    print(i)

for j in Child.keys():
    print(j)
for k in Child.values():
    print(k)
l = []
l.append(k)
print(l)
