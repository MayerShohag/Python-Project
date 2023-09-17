total_money = float(input("Enter Total Money : ")) # Manager total money
total_meal = int(input("Enter Total Meal : ")) # Month total meal
total_meal_rate = float(total_money/total_meal) # total money / total meal

try:
    for i in range(1, 25, 1): 
        name = input("Enter Name : ") 
        money = int(input("Enter Money : "))
        meal = int(input("Enter Meal : "))
        cost = (meal*total_meal_rate) # meal * total meal rate
        mp = int(money-cost) # money-cost
        print("________________________")
        print("Name is : ", name)
        print("Given by the Manager : ", money)
        print("Meal rate is : ", "%.2f" % total_meal_rate)
        print("Meal ate : ", meal)
        print("Cost is : ", "%.2f" % cost)
        print("Manager will give/receive : ", mp)
        print("________________________")
except:
    print("Somethings wrong with you...!")
