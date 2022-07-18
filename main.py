from functools import reduce

# x=0
# while x < 10:
#
#     print(x * " #")
#     x += 1


# Lists
name = ["Zohaib", "Hassan", "Shah"]
print(name)
name[1] = "Awais"
print(name)

print(name[0:2])

name.append("Sohail")
print(name)

name.insert(1, "Ali")
print(name)

# for item in name:
#     print(item)

# {} for Dictionary
# [] for List
# () for tuple
# Key value pairs
# Dictionaries
# d1={"Zohaib":"Brayani", "Hassan":"Pulao","Ali":"Fish"}
# print(d1["Zohaib"])
print("\n")
d1 = {"Zohaib": "Fish",
      "Hassan": "Food",
      "Ali": {"M": "Paratha",
              "L": "Roti",
              "D": "Roast"}}


print(d1["Ali"]["L"])
print("\n", "Update Dict")
# Update
# d1["Awais"] = "Brayani"
d1.update({"Awais": "Brayani"})
print(d1)

del d1["Ali"]
print(d1)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
        }
print(car["year"])

print("\n", "Lambda Function")

"""Lamda Function"""


value = lambda a, b: a*b
print(value(4, 5))

print("\n", "\"Filter Function adult values >18\"")

# Filter Function
ages = [21, 8, 9, 12, 19, 17, 45, 23, 22]
def age_function(value_in_list):
    if value_in_list < 18:
        return False
    else:
        return True


adults = list(filter(age_function, ages))
for values in adults:
    print(values)

print("\n", "Filter through Lambda")

even_values = list(filter(lambda even: even % 2 == 0, ages))
print("Even Values are :")
for values in even_values:
    print(values)

print("\n", "Map through Lambda")

add_1 = list(map(lambda add: add + 1, even_values))
for values_even_list in add_1:
    print("Values after adding 1 in Even List :", values_even_list)


print("\n", "Reduce through Lambda")
sum_no = reduce(lambda a, b: a + b, adults)
print("Addition of adults is", sum_no)

print("\n", "Find Max through Reduce")
max_no = reduce(lambda first_value, sec_value: first_value if first_value > sec_value
                else sec_value, adults)
print("Max in adults is ", max_no)
