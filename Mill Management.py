total_money = float(input("Enter Total Money : "))
total_mill = int(input("Enter Total Mill : "))
total_mill_rate = float(total_money/total_mill)

try:
    for i in range(1, 25, 1):
        name = input("Enter Name : ")
        money = int(input("Enter Money : "))
        mill = int(input("Enter Mill : "))
        cost = (mill*total_mill_rate)
        mp = int(money-cost)
        print("________________________")
        print("Name is : ", name)
        print("Given by the Manager : ", money)
        print("Mill rate is : ", "%.2f" % total_mill_rate)
        print("Mill ate : ", mill)
        print("Cost is : ", "%.2f" % cost)
        print("Manager will give/receive : ", mp)
        print("________________________")
except:
    print("Somethings wrong with you...!")