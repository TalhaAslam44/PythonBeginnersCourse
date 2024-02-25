account_type_list = [
    "Saving",
    "Current"
]
gender = ["MALE", "FEMALE", "OTHER"]
fee = int(input("Enter fee: "))
account_balance = 500

# Function to get valid account type input
def get_account_type():
    while True:
        print("Select Account type: ")
        for index, acc_type in enumerate(account_type_list, start=1):
            print(index, ": ", acc_type)
        select_acc_type = int(input("Select 1 or 2: "))
        if select_acc_type in [1, 2]:
            return account_type_list[select_acc_type - 1]
        else:
            print("Invalid Account Type. Please select 1 or 2.")

# Function to get valid gender input
def get_gender():
    while True:
        print("Select Gender: ")
        for index, g_t in enumerate(gender, start=1):
            print(index, ":", g_t)
        select_gender = int(input("Select gender: "))
        if select_gender in [1, 2, 3]:
            return gender[select_gender - 1]
        else:
            print("Invalid Gender. Please select 1, 2, or 3.")


def withdraw_money(amount):
    global account_balance
    if amount <= account_balance:
        account_balance -= amount
        print("Withdrawal successful.")
    else:
        print("Insufficient funds.")


def deposit_money(amount):
    global account_balance
    account_balance += amount
    print("Deposit successful.")


account_type = get_account_type()
print("Selected Account Type:", account_type)

gender_type = get_gender()
print("Selected Gender:", gender_type)

name_f = input("Enter First Name: ")
name_l = input("Enter Last Name: ")
cnic = input("Enter CNIC: ")
phone_no = input("Enter Phone Number: ")
address_c = input("Enter address: ")
city_c = input("Enter city: ")

while True:
    print("\nOptions:")
    print("1. Withdraw Money")
    print("2. Deposit Money")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter the amount to withdraw: "))
        withdraw_money(amount)
        print("Current Balance:", account_balance)
    elif choice == 2:
        amount = float(input("Enter the amount to deposit: "))
        deposit_money(amount)
        print("Current Balance:", account_balance)
    elif choice == 3:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please choose again.")
