person_info = {
    "person1":{ 
        "Name" : "Alok Biswas",
        "Age" : 19,
        "Profession" : "Programmer",
        "Email" : "alok@gamil.com",
        "Address" : "Barisal Sodor"
    },
    "person2":{ 
        "Name" : "Anik Biswas",
        "Age" : 14,
        "Profession" : "Student",
        "Email" : "anik@gamil.com",
        "Address" : "Barisal Sodor"
    },
    "person3":{ 
        "Name" : "Rakesh ",
        "Age" : 17,
        "Profession" : "Student",
        "Email" : "rakesh@gamil.com",
        "Address" : "Agailjahar, Barisal"
    },
    "person4":{ 
        "Name" : "Ratul Halder",
        "Age" : 20,
        "Profession" : "Data Engineer",
        "Email" : "ratulhalder@gamil.com",
        "Address" : "Gournodi, Barisal"
    },
    "person5":{ 
        "Name" : "Ripon Biswas",
        "Age" : 24,
        "Profession" : "Teacher",
        "Email" : "RiponHalder@gamil.com",
        "Address" : "Banaripara, Barisal",
        "Phone_number": {
            "SIM1": "01709876543",
            "SIM2": "01712345678",
            "SIM3": "01967890765",
            "More SIM": [123412,2432523,3244,354,634534,34,(334,343232,63423,23423,5232)]
        }
    },
    "person6":{ 
        "Name" : "Sourov Biswas",
        "Age" : 29,
        "Profession" : "Business man",
        "Email" : "sourovhalder@gamil.com",
        "Address" : "Mirpur-10, Dhaka"
    }
}

#result = person_info["person5"]["Phone_number"]["More SIM"][6][3]
#print(result)
#
#for x, y in person_info.items():
#    print(f'{x} : {y}\n')


child1 = {
  "name" : "Emil",
  "year" : 2004
}

child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
