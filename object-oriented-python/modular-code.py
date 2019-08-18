def purchase_product(product_type,price,mobile_brand,material):
    if product_type == "Mobile":
        if mobile_brand == "Apple":
            discount = 10
        else:
            discount = 5
        total_price = price - price * discount / 100
    else:
        if material == "leather":
            tax = 5
        else:
            tax = 2
        total_price = price + price * tax / 100
    print("Total price of "+product_type+" is "+str(total_price))

def purchase_mobile(price,brand):
    if brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price = price - price * discount / 100
    print("Total price of Mobile is "+str(total_price))

def purchase_shoe(price, material):
    if material == "leather":
        tax = 5
    else:
        tax = 2
    total_price = price + price * tax / 100
    print("Total price of Shoe is "+str(total_price))

purchase_mobile(20000,"Apple")
purchase_shoe(200,"leather")

