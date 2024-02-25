#name  = Talha Aslam
#Email: john@gmail.com
#Phone: 1234
#customer = {
 #   "name": "Talha Aslam",
 #   "age": 30,
 #   "is_verified": True
#}
#customer ["name"] = "Rana Talha"
#customer
#print(customer.get("birthdate", "may 7 2001"))
#print(customer["name"])

phone = input("phone: ")
digits_mapping = {
    "0": "zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)




