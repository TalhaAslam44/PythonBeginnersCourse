try:
    age = int(input('Age: '))
    income = 20000
    reisk = income/age
    print(age)
except ZeroDivisionError:
    print('You can\'t divide by zero')
except ValueError:
    print("Invalid value")
