print("="*50)
print("         SHOPPING INVOICE")
print("="*50)


print("...Product 01...")
price_1=float(input("Enter Price Rs. : "))
qty_1=int(input("Enter Quentity : "))

print("="*20)

print("...Product 02...")
price_2=float(input("Enter Price Rs. : "))
qty_2=int(input("Enter Quentity : "))

print("="*20)

print("...Product 03...")
price_3=float(input("Enter Price Rs. : "))
qty_3=int(input("Enter Quentity : "))

print("="*20)

print("...Delivary Charge And Discount...")
delivary_fee=float(input("Enter Delivary Fee : "))
discount_presentage=float(input("Enter Discount Presentage : "))

print("="*20)

print("...Subtotal...")
subtotal_1 = price_1 * qty_1
subtotal_2 = price_2 * qty_2
subtotal_3 = price_3 * qty_3
subtotal = subtotal_1 + subtotal_2 + subtotal_3
print("Subtotal is = ",subtotal)

print("="*20)

print("...Discount Amount...")
discount_amount=subtotal * (discount_presentage / 100)
print("Discount Amount is = ",discount_amount)

print("="*20)

print("...Total After Discount...")
after_discount=subtotal-discount_amount
print("Total After Discount is = ",after_discount)

print("="*20)

print("...Final Total...")
final_total = after_discount + delivary_fee
print("Final Total is = ",final_total)

print("="*50)




    
