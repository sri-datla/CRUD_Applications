# Import our database library
import db

import employee
config = db.getConfig()

# Connect to the database
connection = db.connect(config)

choice = ""

while(choice!="q"):
    choice = input("Please enter an option (l) for list employee(i) for insert employee, (e) for edit employee, (d) for delete employee, (em) to generate email address ,(q) for end")
    match choice:
        case "l":
            print("List employees")
            employee.list_employees(connection)
        case "i":
            print("Insert employees")
            employee.insert_employee(connection)
        case "e":
            print("Edit employee")
            employee.edit_employee(connection)
        case "d":
            print("delete employee")
            employee.delete_employee(connection)
        case "q":
            print("Thank you, come again!")
            db.disconnect(connection)
        case "em":
            print("Generating email addresses")
            # if same email exists then add 1 or 2 at the end
            employee.generate_email_list(connection)
