my_dict = {
    "name" : "anum",
    "age" : 29,
    "city" : "karachi",
}


# keys:
print(my_dict.keys())


#values:
print(my_dict.values())


# items:
print(my_dict.items())


# get:
print(my_dict.get("name"))


# updated:
new_dict = {"city" : "islamabad"}
my_dict.update(new_dict)
print(my_dict)


# pop:
print(my_dict.pop("city"))
print(my_dict)


# clear:
my_dict.clear()
print(my_dict)