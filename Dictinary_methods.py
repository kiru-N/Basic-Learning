dict1 = {'Ram': 80, 'Syam': 96, 'Kavin': 97}
print(dict1)

# print(*dict1.values())
print(dict1)
for key, values in dict1.items():
    # print(f'{items}: {dict1[items]}')
    print(key, ":", values)
    print(97 in dict1.values())

shop = {'apple': 100, 'banana': 30, 'orange': 40, 'papaya': 25}

for fruits, price in shop.items():
    shop[fruits] = round(price * 1.1, 2)
print(shop)

employee = {'kathir': 101, 'kesavan': 103, 'seeta': 105, 'kathir': 201}
new_emp = {}

for key, value in employee.items():
    new_emp[value] = key

print(new_emp)

employee = {'kathir': 3000, 'kesavan': 7000, 'seeta': 5000, 'Arul': 2800,
            'Anjana':4000}
# new_emp = {}
total_income = 0
for values in employee.values():
    total_income += values