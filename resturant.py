orderid=0
while True:    
    orderid=orderid+1
    print("--------------------------------------------------------------")
    print("\t\t     ABC Restaurant")
    print("--------------------------------------------------------------")
    print("Types of Recipe")
    print("--------------------------------------------------------------")
    print("1. Fruit Juice")
    print("2. Chinese")
    print("3. Soup")
    print("4. Tandoori Snacks")
    print("5. Tandoori")
    print("6. North Indian")
    print("7. Ice Cream")
    print("8. Milk Shake")
    print("--------------------------------------------------------------")
    while True:
        num = int(input("Enter the Recipe Number: "))
    
        if num>8 and num==0:
            break

        elif num == 1:
            print("1. Orange : 40.00")
            print("2. Mango : 45.00")
            print("3. Watermelon : 45.00")
            print("4. Lemon : 35.00")
            print("5. Pineapple : 40.00")
            print("6. Musambi : 40.00")

        elif num == 2:
            print("7. Gobi Manchuri : 70.00")
            print("8. Gobi Manchuri-Half : 40.00")
            print("9. Gobi Chilli : 75.00")
            print("10. Gobi 65 : 80.00")
            print("11. Paneer Manchuri : 95.00")
            print("12. Paneer Chilli : 100.00")
            print("13. Paneer 65 : 100.00")
            print("14. Paneer Pepper Dry : 110.00")

        elif num == 3:
            print("15. Hot and Sour Soup : 60.00")
            print("16. Veg Mancho Soup : 65.00")
            print("17. Mushroom Soup : 65.00")

        elif num == 4:
            print("18. Paneer Tikka : 130.00")
            print("19. Mushroom Tikka : 130.00")
            print("20. Baby Corn Tikka :120.00")

        elif num == 5:
            print("21. Roti : 20.00")
            print("22. Butter Roti : 25.00")
            print("23. Kulcha : 25.00")
            print("24. Butter Kulcha : 28.00")
            print("25. Naan : 30")
            print("26. Butter Naan : 35.00")
            print("27. Parota : 25.00")
            print("28. Butter Parota : 30.00")
            print("29. Alu Parota : 40.00")
            print("30. Veg Stuffed Parota : 45.00")
            print("31. Veg Stuffed Kulcha : 45.00")

        elif num == 6:
            print("32. Kaju Masala : 160.00")
            print("33. Paneer Butter Masala : 135.00")
            print("34. Mushroom Masala : 130.00")
            print("35. Veg Kadai : 115.00")
            print("36. Veg Kolhapuri : 110.00")
            print("37. Veg Hyderbadi : 110.00")
            print("38. Capsicum Masala : 110.00")
            print("39. Roti Curry : 50.00")
            print("40. Tomato Curry : 100.00")
            print("41. Palak Paneer : 110.00")

        elif num == 7:
            print("42. Vanilla : 35.00")
            print("43. Chocolate : 40.00")
            print("44. Pista : 45.00")
            print("45. Strawberry : 40.00")
            print("46. Mango : 40.00")
            print("47. Bursraj : 40.00")
            print("48. Gadbad : 70.00")

        elif num == 8:
            print("49. Apple : 70.00")
            print("50. Banana : 50.00")
            print("51. Chocolate : 65.0")
            print("52. Butterscotch : 65.0")
            print("53. Pista : 65.00")
            print("54. Vanilla : 60.00")
            print("55. Strawberry : 60.0")
            print("56. Mango : 60.00")
            
        else:
            break

        
    
    orders = { 1: ("Orange", 40.00), 
              2: ("Mango", 45.00), 
              3: ("Watermelon", 45.00), 
              4: ("Lemon", 35.00), 
              5: ("Pineapple", 40.00), 
              6: ("Musambi", 40.00), 
              7: ("Gobi Manchuri", 70.00), 
              8: ("Gobi Manchuri-Half", 40.00), 
              9: ("Gobi Chilli", 75.00), 
              10: ("Gobi 65", 80.00), 
              11: ("Paneer Manchuri", 95.00), 
              12: ("Paneer Chilli", 100.00), 
              13: ("Paneer 65", 100.00), 
              14: ("Paneer Pepper Dry", 110.00), 
              15: ("Hot and Sour Soup", 60.00), 
              16: ("Veg Mancho Soup", 65.00), 
              17: ("Mushroom Soup", 65.00), 
              18: ("Paneer Tikka", 130.00), 
              19: ("Mushroom Tikka", 130.00), 
              20: ("Baby Corn Tikka", 120.00), 
              21: ("Roti", 20.00), 
              22: ("Butter Roti", 25.00), 
              23: ("Kulcha", 25.00), 
              24: ("Butter Kulcha", 28.00), 
              25: ("Naan", 30.00), 
              26: ("Butter Naan", 35.00), 
              27: ("Parota", 25.00), 
              28: ("Butter Parota", 30.00), 
              29: ("Alu Parota", 40.00), 
              30: ("Veg Stuffed Parota", 45.00), 
              31: ("Veg Stuffed Kulcha", 45.00), 
              32: ("Kaju Masala", 160.00), 
              33: ("Paneer Butter Masala", 135.00), 
              34: ("Mushroom Masala", 130.00), 
              35: ("Veg Kadai", 115.00), 
              36: ("Veg Kolhapuri", 110.00), 
              37: ("Veg Hyderabadi", 110.00), 
              38: ("Capsicum Masala", 110.00), 
              39: ("Roti Curry", 50.00), 
              40: ("Tomato Curry", 100.00), 
              41: ("Palak Paneer", 110.00), 
              42: ("Vanilla", 35.00), 
              43: ("Chocolate", 40.00), 
              44: ("Pista", 45.00), 
              45: ("Strawberry", 40.00), 
              46: ("Mango", 40.00), 
              47: ("Bursraj", 40.00), 
              48: ("Gadbad", 70.00), 
              49: ("Apple", 70.00), 
              50: ("Banana", 50.00), 
              51: ("Chocolate", 65.00), 
              52: ("Butterscotch", 65.00), 
              53: ("Pista", 65.00), 
              54: ("Vanilla", 60.00), 
              55: ("Strawberry", 60.00), 
              56: ("Mango", 60.00) }
    
    
    totalprice = 0
    totalgst = 0
    all_orders = []
    
    while True:
        choice = list(map(int, input("Enter the Order Nos you wish to: ").split()))
        quantities = list(map(int, input("Enter the quantities for each order: ").split()))
    
        ordertotal = 0
        ordergst = 0
    
        print("\nOrder Summary:")
        print("--------------------------------------------------------------")
        print("OrderNo         Item         Quantity   Price    GST   Total")
        print("--------------------------------------------------------------")
        
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

        print("--------------------------------------------------------------")
        print(f"Order Total Price: {ordertotal:.2f}")
        print(f"Order GST: {ordergst:.2f}")
        print(f"Cumulative Total Price: {totalprice:.2f}")
        print(f"Cumulative GST: {totalgst:.2f}")
        print(f"Grand Total: {gtotal:.2f}")
        print("--------------------------------------------------------------")
    
        order2 = input("Would you like to place another order? If yes, press 1: ")
        if order2 != '1':
            print("Thank you for your order!")
            print("--------------------------------------------------------------")
            print("\t\t      Final Bill")
            print("--------------------------------------------------------------")
            print("\t\t     ABC Restaurant")
            print("--------------------------------------------------------------")
            print("Order ID:",id(orderid))
            print("--------------------------------------------------------------")
            print("OrderNo         Item         Quantity   Price    GST   Total")
            print("--------------------------------------------------------------")
            for order in all_orders:
                num, item, qty, price, gst, total = order
                print(f"{num:<9}{item:<22}{qty:<9}{price:<9}{gst:<7}{total:<9}")
            print("--------------------------------------------------------------")
            print(f"Final Total Price: {totalprice:.2f}")
            print(f"Final Total GST: {totalgst:.2f}")
            print(f"Grand Total: {gtotal:.2f}")
            print("--------------------------------------------------------------")
            print("\t\t    Thank You Visit Again")
            print("--------------------------------------------------------------")
            break
