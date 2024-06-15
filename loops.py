snacks =[
    {
       "item name": "string" ,
       "price": float,
       "Quantity": int
    }
]

item ={
       "item name": "Pizza",
       "price": 3.7,
       "Quantity": 3
    }

item2 ={
       "item name": "Burger",
       "price": 3.6,
       "Quantity": 2
    }
snacks.append(item)
snacks.append(item2)

for snack in snacks:
    #save the item name , price and qty as variables
    item_name=snack["item name"]
    price=snack["price"]
    qty= snack["Quantity"]
    print(f"Snack : {item_name}, price :  {price} , Quantity : {qty}")



