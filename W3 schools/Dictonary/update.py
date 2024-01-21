company = {"Compeny":{
                "Emlpolly ":{"Detail":[{"1st":
                    {"Name": "Ashok Mojumdar",
                                    "Position": "Junior Software Engineer",
                                    "Sallary": 30000,
                                    "Address": "Dhaka, Motijhil"}},
                        {"2nd":
                        {"Name": "Ashok Mojumdar",
                                    "Position": "Senior Software Engineer",
                                    "Sallary": 50000,
                                    "Address": "Barisal, Agailjhar, Askar"}},
                        {"3rd":
                        {"Name": "Shiab Islam",
                                    "Position": "Senior Software Engineer",
                                    "Sallary": 50000,
                                    "Address": "Rajsahi, Nilpur" }}]}}}


print(company.items())
print("\n")
print(company.update({"CEO":"Alex"}))