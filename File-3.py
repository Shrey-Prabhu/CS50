members = [     #{key: value}
    {"relation": "son",  "name": "Shrey"},      #member 1
    {"relation": "daughter", "name": "Sarika"}      #member 2

]


for member in members:
    print(member["name"], member["relation"], sep = "\t")#member[key] =>value