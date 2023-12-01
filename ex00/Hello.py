ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"} # can only have unique values
ft_dict = {"Hello" : "titi!"}

# change the value of the list
ft_list[1] = "World!"


# change the value of the tuple
ft_tuple_tmp = list(ft_tuple)
ft_tuple_tmp[1] = "France!"
ft_tuple = tuple(ft_tuple_tmp)

# change the value of the set
ft_set.remove("tutu!")
ft_set.add("Paris!")

# change the value of the dict
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
