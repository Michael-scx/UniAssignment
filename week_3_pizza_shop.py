

print(" === Pizza Shop Order System === ")
print("Enter pizza size: personal, medium, or family ")
print("Type 'done' when finished ordering")

per = 7
med = 12
family = 18
total = 0
while True :
    a = input("\nEnter pizza size : ")
    if a == "done" :
        break
    elif a == "personal" :
        total+=7
        print(f"Price: $7.00")
    elif a == "medium" :
        total+=12
        print(f"Price: $12.00")
    elif a == "family" :
        total+=18
        print("Price: $18.00")
    else :
        print("Please choose - personal , medium , family only")
    print(f"Current Total: ${total:.2f}")

if total >= 40 :
    b = total - 5.00
    print("\n === Order Summary === ")
    print(f"Subtotal : ${total:.2f} ")
    print("Party Order Discount : -$5.00 ")
    print(f"Final Total : ${b:.2f}")
    print("Thank you for your order!")
else : 
    print("Party Order Discount : $0.00")
    print(f"Final Total : ${total:.2f}")
    print("Thank you for your order!")






