cart = []
while True:
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. Display Cart")
    print("4. Display Total Items")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        product = input("Enter product name: ")
        cart.append(product)
        print("Product added to cart.")
    elif choice == "2":
        product = input("Enter product name to remove: ")
        if product in cart:
            cart.remove(product)
            print("Product removed from cart.")
        else:
            print("Product not found in cart.")
    elif choice == "3":
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            print("Products in Cart:")
            for item in cart:
                print(item)
    elif choice == "4":
        print("Total items in cart:", len(cart))
    elif choice == "5":
        print("Exiting application.")
        break
    else:
        print("Invalid choice.")