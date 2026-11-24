customer_name = input("Enter customer name: ")
item_name = input("Enter food item: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
phone_number = input("Enter phone number: ")
table_number = int(input("Enter table number: "))
payment_method = input("Enter payment method: ")
discount = float(input("Enter discount: "))
delivery_type = input("Enter delivery type: ")
order_id = input("Enter order ID: ")

total = quantity * price
final_bill = total - discount

print("\n--- Order Details ---")
print("Customer Name:", customer_name)
print("Food Item:", item_name)
print("Quantity:", quantity)
print("Price per item:", price)
print("Phone Number:", phone_number)
print("Table Number:", table_number)
print("Payment Method:", payment_method)
print("Discount:", discount)
print("Delivery Type:", delivery_type)
print("Order ID:", order_id)
print("Total Bill:", total)
print("Final Bill:", final_bill)
with open("orders.txt", "a") as f:
    f.write(f"{customer_name}, {item_name}, {quantity}, {price}, "
            f"{phone_number}, {table_number}, {payment_method}, "
            f"{discount}, {delivery_type}, {order_id}, {final_bill}\n")
print("\nOrder saved successfully!") 
customer_name = input("Enter customer name: ")
item_name = input("Enter food item: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
phone_number = input("Enter phone number: ")
table_number = int(input("Enter table number: "))
payment_method = input("Enter payment method: ")
discount = float(input("Enter discount: "))
delivery_type = input("Enter delivery type: ")
order_id = input("Enter order ID: ")

total = quantity * price
final_bill = total - discount

print("\n--- Order Details ---")
print("Customer Name:", customer_name)
print("Food Item:", item_name)
print("Quantity:", quantity)
print("Price per item:", price)
print("Phone Number:", phone_number)
print("Table Number:", table_number)
print("Payment Method:", payment_method)
print("Discount:", discount)
print("Delivery Type:", delivery_type)
print("Order ID:", order_id)
print("Total Bill:", total)
print("Final Bill:", final_bill)
with open("orders.txt", "a") as f:
    f.write(f"{customer_name}, {item_name}, {quantity}, {price}, "
            f"{phone_number}, {table_number}, {payment_method}, "
            f"{discount}, {delivery_type}, {order_id}, {final_bill}\n")
print("\nOrder saved successfully!") 
