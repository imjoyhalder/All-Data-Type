dictionary = {"Team":["Argentina","Brazil","France","England",],
            "Win":{"Argentina":4,
                    "Brazil":3,
                    "France":3,
                    "Portugal":3}}
k = dictionary.get("Team")
print(k)
j = dictionary.get("Win")
print(j["Argentina"])
print(j["Brazil"])