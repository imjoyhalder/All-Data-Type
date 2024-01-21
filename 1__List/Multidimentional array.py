
print("\n")

ide = int(input("Enter your ide number: "))
cal = -1

array = [
    {"221":{"Name":"Bishow",
            "Board roll": 2166209,
            "Age": 16,
            "Address": "Sador,Barisal",
            "Modile": "01475140896"}
            },

    {"222":{"Name":"Joy",
            "Board roll": 2166210,
            "Age": 18,
            "Address": "Agailjhara,Barisal",
            "Modile": "01689574237"}
            },
            
    {"223":{"Name":"Niloy",
            "Board roll": 2166211,
            "Age": 15,
            "Address": "Baropaika,Barisal",
            "Modile": "01908974254"}
            },
    {"224":{"Name":"Meraj",
            "Board roll": 2166249,
            "Age": 16,
            "Address": "Notun Bazar,Barisal",
            "Modile": "01748934567"}
            },
    {"225":{"Name":"Abir",
            "Board roll": 2166249,
            "Age": 16,
            "Address": "Rupatoli,Barisal",
            "Modile": "01740896780"}
            },
    {"226":{"Name":"Alex",
            "Board roll": 6209,
            "Age": 16,
            "Address": "Nimtola,Barisal",
            "Modile": "01740995732"}
            },
]
b = ide-220
print('Student Information',"\n")
if ide>220:
    cal = cal+b
    a = array[cal].values()
    for i in tuple(a):
        p =i.items()
        for j in p:
                k = str(j)
                print(k)

else:
    print("Not found")