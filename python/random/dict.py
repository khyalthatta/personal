
# Student Registration Form



while True:
    student_dict = {'name': input("Enter Your Name"), 'age': input("Enter Your Age: "), 'address': input("Enter Your Address")}

    decision = input("You still want to continue or not? yes/no:  ")

    if decision.lower() == 'yes':
        continue

    else:
        break

print(student_dict)
