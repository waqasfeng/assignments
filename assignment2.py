user = int(input("enter an integer: "))
rng = int(input("great, now tell me the range uptill which you wanna display the table: "))
for i in range(1,rng + 1):
    product = user * i
    print(f"{user} x {i} = {product}")
