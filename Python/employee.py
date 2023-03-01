
def list_employees(conn):
    
    list_employees_cursor = conn.cursor()

    list_query = """SELECT employee_id, first_name,
                            last_name,
                            salary,
                            employee_type
                                FROM employee;"""
    list_employees_cursor.execute(list_query)

    for x in list_employees_cursor:
        print(x)
    list_employees_cursor.close()

def insert_employee(conn):
    first_name = input("Please enter the first name: ")
    last_name = input("Please enter the last name: ")
    salary = input("Please enter the salary for the user")
    employee_type = input("Please enter the employee type (Manager, Administrator, Operational)")

    insert_employee_query = """INSERT INTO employee (first_name, last_name, salary, employee_type)
                            VALUES (%s, %s, %s, %s)"""
    
    employee_values = (first_name, last_name, float(salary), employee_type)
    insert_employee_cursor = conn.cursor()

    insert_employee_cursor.execute(insert_employee_query, employee_values)
    

    conn.commit()
    insert_employee_cursor.close()
    print("employee successfully inserted")


def delete_employee(conn):
    emp_id = input("please enter employee id of the employee to delete from table")

    delete_employee_query = """
    DELETE FROM employee WHERE employee_id = %s
    """ %(emp_id)
    

    delete_employee_cursor = conn.cursor()

    delete_employee_cursor.execute(delete_employee_query)

    conn.commit()
    delete_employee_cursor.close()
    print("Employee successfully deleted")


def edit_employee(conn):
    emp_id = input("Please enter the employee id of the employee to edit the value")
    choice = input("Please press f to update first name, l to update last name s to update salary")
    match choice:
        case "f":
            frst_name = input("Please enter first name")
            update_query = """UPDATE employee SET first_name = %s WHERE employee_id = %s"""
            update_values = (frst_name,emp_id)
            print(update_query)
        case "l":
            last_name = input("Please enter last name")
            update_query = """UPDATE employee SET last_name = %s WHERE employee_id = %s""" %(last_name,emp_id)
            update_values = (last_name,emp_id)
        case "s":
            salary = input("Please enter new salary")
            update_query = """UPDATE employee SET salary = %s WHERE employee_id = %s""" %(salary,emp_id)
            update_values = (salary,emp_id)
              

    update_employee_cursor = conn.cursor()
    update_employee_cursor.execute(update_query,update_values)

    conn.commit()
    update_employee_cursor.close()
    print("Record updated")
    
    
def generate_email_list(conn):
    generate_email_list_cursor = conn.cursor()
    sql_email_list = """ SELECT generate_email(first_name, last_name) FROM employee;"""
    generate_email_list_cursor.execute(sql_email_list)

    for e in generate_email_list_cursor:
        print(e)
    generate_email_list_cursor.close()