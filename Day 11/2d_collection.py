# #  2d collection 

# fruits =     ["apple" , "banana" , "orange" , "coconut" ]
# vegetables = ["celery" , "tomato" , "carrot" , "potatoe"]
# meats =      ["chicken" , "fish" , "goat"]

# groceries = [fruits,vegetables,meats]

# # print(groceries[2][2])

# for collection in groceries:
#     for food in collection:
#         print(food, end = " ")
#     print()

# Num Pad

num_pad = ((1 , 2 , 3),
           (4 , 5 , 6),
           (7 , 8 , 9),
           ('#', 0 , '*'))

for row in num_pad:
    for num in row:
        print(num, end = " ")
    print()
