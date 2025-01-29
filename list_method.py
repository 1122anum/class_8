my_list = ["babar", "anum", "zayaan","yamaan","emaan"]
print(my_list)
my_list.append("grand perants")
print(my_list)

# insert
my_list.insert(1, "sir zia")
print(my_list)


# reverse
my_list.reverse()
print(my_list)


# pop
my_list.pop()
print(my_list)


# remove
my_list.remove("sir zia")
print(my_list)

# sort
my_list.sort(reverse=True)
print(my_list)


# extend
new_list = ["abdullah", "ghous"]
print("old list", my_list)
my_list.extend(new_list)
print("updated list", my_list)