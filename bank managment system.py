account_type_list = [
    "Saving",
    "Current"
]
account_type = ""
gender = ["MALE", "FEMALE", "OTHER"]
fee = 0
account_balance = 0
print("Select Account type: ")
inc = 1
for acc_type in account_type_list:
    print(inc, ": ", acc_type)
    inc += 1
select_Acc_type = int(input("Select 1 or 2 : "))

if select_Acc_type == 1:
    account_type = account_type_list[0]
elif select_Acc_type == 2:
    account_type = account_type_list[1]
else:
    print("Wrong Account Type")
print(account_type)

gender_type = ""
print("Select Gender : ")
g_inc = 1
for g_t in gender:
    print(g_inc, " : ", g_t)
    g_inc += 1

select_gender = int(input("Select gender: "))

if select_gender == 1:
    gender_type = gender[0]
elif select_gender == 2:
    gender_type = gender[1]
elif select_gender == 3:
    gender_type = gender[2]
else:
    print("Invlaid gender type")
print(gender_type)

name_f = input("Enter First Name: ")
name_l = input("Enter Last Name : ")
cnic = input("Enter CNIC : ")
phone_no = input("Enter Phone Number : ")
address_c = input("Enter address : ")
city_c = input("Enter city :")

