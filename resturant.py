orderid=0
while True:    
    orderid=orderid+1
    print("--------------------------------------------")
    print("\tDSU Restaurant")
    print("--------------------------------------------")
    print("Types of Recipe")
    print("--------------------------------------------")
    print("1. Biriyani")
    print("2. Fried Rice")
    print("3. Noodles and Gobi")
    print("4. Egg")
    print("5. Veg North Indian")
    print("6. Chicken(Indian,Chinese,Tandoori)")
    print("--------------------------------------------")
    while True:
        num = int(input("Enter the Recipe Number: "))
    
        if num>6 and num==0:
            break

        elif num == 1:
            print("1. Hyderabadi Biryani : 120.0")
            print("2. Egg Biryani : 110.0")
            print("3. Veg Biryani : 80.00")
            print("4. Biryani Rice : 60.00")
            print("5. Ghee Rice : 60.00")
            print("6. Jeera Rice : 50.00")
            print("7. White Rice Meals : 60.00")
            print("8. Boil Rice Meals : 60.00")

        elif num == 2:
            print("9. Chicken Fried Rice : 80.00")
            print("10. Egg Fried Rice : 60.00")
            print("11. Veg Fried Rice : 50.00")
            print("12. Gobi Fried Rice : 70.00")
            print("13. Paneer Fried Rice : 80.00")
            print("14. Mushroom Fried Rice : 80.00")

        elif num == 3:
            print("15. Chicken Noodles : 90.00")
            print("16. Egg Noodles : 60.00")
            print("17. Veg Noodles : 50.00")
            print("18. Paneer Noodles : 80.00")
            print("19. Gobi Noodles : 70.00")
            print("20. Gobi Manchurian : 50.00")
            print("21. Gobi Chilly : 60.00")
            print("22. Egg Gobi Manchurian : 80.00")

        elif num == 4:
            print("23. Omlet : 30.00")
            print("24. Egg Burji : 60.00")
            print("25. Egg Chilly : 70.00")
            print("26. Egg Masala : 50.00")
            print("27. Egg Roast : 70.00")
            print("28. Boiled Egg (2 piece) : 25.00")
            print("29. Egg Bulsi (2 piece) : 30.00")

        elif num == 5:
            print("30. Paneer Butter Masala : 80.00")
            print("31. Sayi Paneer : 80.00")
            print("32. Kema Paneer : 80.00")
            print("33. Paneer Burji : 80.00")
            print("34. Palak Paneer : 80.00")
            print("35. Mattar Paneer : 80.00")
            print("36. Paneer Chilly : 80.00")
            print("37. Paneer Manchurian : 80.00")
            print("38. Dal Fry Tadka : 50.00")
            print("39. Tomato Fry : 50.00")
            print("40. Green Peas Masala : 50.00")
            print("41. Channa Masala : 50.00")
            print("42. Rajma Masala : 50.00")
            print("43. Bhedi Masala : 50.00")
            print("44. Bagah Masala : 60.00")
            print("45. Bhedi Fry : 50.00")
            print("46. Capsicum Masala : 80.00")
            print("47. Mushroom Masala : 90.00")
            print("48. Mushroom Fry : 90.00")
            print("49. Mix Sabzi : 60.00")
            print("50. Aloo Gobi Sabzi : 60.00")

        elif num == 6:
            print("51. Tandoori Chicken (full) : 280.0")
            print("52. Chicken Tikka : 180.0")
            print("53. Butter Chicken : 90.00")
            print("54. Chicken 65 : 90.00")
            print("55. Chicken 65 Fry : 100.0")
            print("56. Chicken Masala : 80.00")
            print("57. Chicken Hyderabad : 130.0")
            print("58. Chicken Chilly : 90.00")
            print("59. Ginger Chicken : 80.00")
            print("60. Garlic Chicken : 80.00")
            print("61. Chicken Manchurian : 80.00")
            print("62. Lemon Chicken : 80.00")
            print("63. Chicken Pepper Fry : 80.00")
            print("64. Chicken Pepper Curry : 85.00")
            print("65. Chicken Fry : 80.00")
            print("66. Chicken Kabab : 70.00")
            print("67. Kalmi Kabab (1 pcs) : 60.00")
            print("68. Chicken Padees : 80.00")
            print("69. Chicken Keema : 130.0")
            print("70. Chicken Edakkd : 280.0")
            print("71. Chicken Kanoor Masala : 380.0")
            print("72. Chicken Talashary : 380.0")
            print("73. Chicken Kadambur : 380.0")
        else:
            break

        
    
    orders = {
    1: ("Hyderabadi Biryani", 120.0),
    2: ("Egg Biryani", 110.0),
    3: ("Veg Biryani", 80.00),
    4: ("Biryani Rice", 60.00),
    5: ("Ghee Rice", 60.00),
    6: ("Jeera Rice", 50.00),
    7: ("White Rice Meals", 60.00),
    8: ("Boil Rice Meals", 60.00),
    9: ("Chicken Fried Rice", 80.00),
    10: ("Egg Fried Rice", 60.00),
    11: ("Veg Fried Rice", 50.00),
    12: ("Gobi Fried Rice", 70.00),
    13: ("Paneer Fried Rice", 80.00),
    14: ("Mushroom Fried Rice", 80.00),
    15: ("Chicken Noodles", 90.00),
    16: ("Egg Noodles", 60.00),
    17: ("Veg Noodles", 50.00),
    18: ("Paneer Noodles", 80.00),
    19: ("Gobi Noodles", 70.00),
    20: ("Gobi Manchurian", 50.00),
    21: ("Gobi Chilly", 60.00),
    22: ("Egg Gobi Manchurian", 80.00),
    23: ("Omlet", 30.00),
    24: ("Egg Burji", 60.00),
    25: ("Egg Chilly", 70.00),
    26: ("Egg Masala", 50.00),
    27: ("Egg Roast", 70.00),
    28: ("Boiled Egg (2 piece)", 25.00),
    29: ("Egg Bulsi (2 piece)", 30.00),
    30: ("Paneer Butter Masala", 80.00),
    31: ("Sayi Paneer", 80.00),
    32: ("Kema Paneer", 80.00),
    33: ("Paneer Burji", 80.00),
    34: ("Palak Paneer", 80.00),
    35: ("Mattar Paneer", 80.00),
    36: ("Paneer Chilly", 80.00),
    37: ("Paneer Manchurian", 80.00),
    38: ("Dal Fry Tadka", 50.00),
    39: ("Tomato Fry", 50.00),
    40: ("Green Peas Masala", 50.00),
    41: ("Channa Masala", 50.00),
    42: ("Rajma Masala", 50.00),
    43: ("Bhedi Masala", 50.00),
    44: ("Bagah Masala", 60.00),
    45: ("Bhedi Fry", 50.00),
    46: ("Capsicum Masala", 80.00),
    47: ("Mushroom Masala", 90.00),
    48: ("Mushroom Fry", 90.00),
    49: ("Mix Sabzi", 60.00),
    50: ("Aloo Gobi Sabzi", 60.00),
    51: ("Tandoori Chicken (full)", 280.0),
    52: ("Chicken Tikka", 180.0),
    53: ("Butter Chicken", 90.00),
    54: ("Chicken 65", 90.00),
    55: ("Chicken 65 Fry", 100.0),
    56: ("Chicken Masala", 80.00),
    57: ("Chicken Hyderabad", 130.0),
    58: ("Chicken Chilly", 90.00),
    59: ("Ginger Chicken", 80.00),
    60: ("Garlic Chicken", 80.00),
    61: ("Chicken Manchurian", 80.00),
    62: ("Lemon Chicken", 80.00),
    63: ("Chicken Pepper Fry", 80.00),
    64: ("Chicken Pepper Curry", 85.00),
    65: ("Chicken Fry", 80.00),
    66: ("Chicken Kabab", 70.00),
    67: ("Kalmi Kabab (1 pcs)", 60.00),
    68: ("Chicken Padees", 80.00),
    69: ("Chicken Keema", 130.0),
    70: ("Chicken Edakkd", 280.0),
    71: ("Chicken Kanoor Masala", 380.0),
    72: ("Chicken Talashary", 380.0),
    73: ("Chicken Kadambur", 380.0)
}
    
    
    totalprice = 0
    totalgst = 0
    all_orders = []
    
    while True:
        choice = list(map(int, input("Enter the Order Nos you wish to: ").split()))
        quantities = list(map(int, input("Enter the quantities for each order: ").split()))
    
        ordertotal = 0
        ordergst = 0
    
        print("\nOrder Summary:")
        print("--------------------------------------------")
        print("OrderNo         Item         Quantity   Price    GST   Total")
        print("--------------------------------------------")
        
        for num, qty in zip(choice, quantities):
                if num in orders:
                    item, price = orders[num]
                    totalitem = price * qty
                    gst = totalitem * 0.05
                    total = totalitem + gst
                    print(f"{num:<9}{item:<22}{qty:<9}{price:<9}{gst:<7}{total:<9}")
                    all_orders.append((num, item, qty, price, gst, total))
                    ordertotal += totalitem
                    ordergst += gst
                else:
                    print(f"{num}. Invalid Order Number")
    
        totalprice += ordertotal
        totalgst += ordergst
        gtotal = totalprice + totalgst

        print("--------------------------------------------")
        print(f"Order Total Price: {ordertotal:.2f}")
        print(f"Order GST: {ordergst:.2f}")
        print(f"Cumulative Total Price: {totalprice:.2f}")
        print(f"Cumulative GST: {totalgst:.2f}")
        print(f"Grand Total: {gtotal:.2f}")
        print("--------------------------------------------")
    
        order2 = input("Would you like to place another order? If yes, press 1: ")
        if order2 != '1':
            print("Thank you for your order!")
            print("--------------------------------------------")
            print("\t     Final Bill")
            print("--------------------------------------------")
            print("\t   DSU Restaurant")
            print("--------------------------------------------")
            print("Order ID:",id(orderid))
            print("--------------------------------------------")
            print("OrderNo  Item  Quantity  Price   GST   Total")
            print("--------------------------------------------")
            for order in all_orders:
                num, item, qty, price, gst, total = order
                print(f"{num:<9}{item:<22}{qty:<9}{price:<9}{gst:<7}{total:<9}")
            print("--------------------------------------------")
            print(f"Final Total Price: {totalprice:.2f}")
            print(f"Final Total GST: {totalgst:.2f}")
            print(f"Grand Total: {gtotal:.2f}")
            print("--------------------------------------------")
            print("\t   Thank You Visit Again")
            print("--------------------------------------------")
            break
