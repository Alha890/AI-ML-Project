employees = []
while True:
    print("\n1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter employee name: ")
        age = input("Enter employee age: ")
        department = input("Enter department: ")
        employee = {
            "Name": name,
            "Age": age,
            "Department": department
        }
        employees.append(employee)
        print("Employee added successfully.")
    elif choice == "2":
        if len(employees) == 0:
            print("No employees found.")
        else:
            for emp in employees:
                print(emp)
    elif choice == "3":
        search_name = input("Enter employee name to search: ")
        found = False
        for emp in employees:
            if emp["Name"].lower() == search_name.lower():
                print("Employee Found:")
                print(emp)
                found = True
                break
        if not found:
            print("Employee not found.")
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")