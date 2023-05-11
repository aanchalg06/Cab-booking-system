import mysql.connector
import datetime

def main_menu():
    print("Welcome to AAggyy Cabs!")
    print("Login as: ")
    print("1. Admin")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        admin_login()
    elif choice == "2":
        login_menu()
    elif choice == "3":
        print("Thank you for using our app!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def admin_login():
    print("Admin Login")
    username = input("Enter username: ")
    password = input("Enter password: ")

    mycursor.execute("SELECT * FROM Admin WHERE username = %s AND password = %s", (username, password))
    
    # get the results of the query
    user = mycursor.fetchone()
    
    if user:
        admin_menu()
    else:
        print("Invalid username or password. Please try again.")
        main_menu()

# Define the admin menu function
def admin_menu():
    print("Admin Menu")
    print("1. View rides")
    print("2. View taxis")
    print("3. View customers")
    print("4. View drivers")
    print("5. Remove taxi")
    print("6. Remove driver")
    print("7. Add taxi")
    print("8. Add driver")
    print("9. Back to main menu")
    choice = input("Enter your choice: ")
    if choice == "1":
        view_rides()
    elif choice == "2":
        view_taxis()
    elif choice == "3":
        view_customers()
    elif choice == "4":
        view_drivers()
    elif choice == "5":
        remove_taxi()
    elif choice == "6":
        remove_driver()
    elif choice == "7":
        add_taxi()
    elif choice == "8":
        add_driver()
    elif choice == "9":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        admin_menu()

# Define the view taxis function
def view_taxis():
    print("Taxis Data")
    # Read taxis data from CSV file and display it here
    # with open('taxis.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         print(row)
    # cursors = mycursor.cursor()
    mycursor.execute("SELECT * FROM Taxi")
    print("current data of taxis owned")
    col_names = [i[0] for i in mycursor.description]

    output = mycursor.fetchall()
    
    print(col_names)
    for i in range(len(output)):
        print(output[i])
    
    # get the results of the query
    admin_menu()

# Define the view customers function
def view_customers():
    print("Customers Data")
    # Read customers data from CSV file and display it here
    # with open('customers.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         print(row)
    mycursor.execute("SELECT * FROM customer")
    print("current data of customers signed up")
    # print('\n')
    col_names = [i[0] for i in mycursor.description]

    output = mycursor.fetchall()
    
    print(col_names)
    for i in range(len(output)):
        print(output[i])
    admin_menu()

def view_rides():
    print("Rides Data")
    # Read rides data from CSV file and display it here
    # with open('rides.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         print(row)
    # print("Taxis Data")
    # Read taxis data from CSV file and display it here
    # with open('taxis.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         print(row)
    # cursors = mycursor.cursor()
    mycursor.execute("SELECT * FROM rides_data as r join payments as p on r.travel_id = p.travel_id")
    print("data of customers along with rides they travelled")
    # print('\n')
    col_names = [i[0] for i in mycursor.description]

    output = mycursor.fetchall()
    
    print(col_names)
    for i in range(len(output)):
        print(output[i])
    
    # get the results of the query
    # admin_menu()
    admin_menu()

# Define the view drivers function
def view_drivers():
    print("Drivers Data")
    # Read drivers data from CSV file and display it here
    # with open('drivers.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         print(row)
    mycursor.execute("SELECT * FROM driver")
    # print("current data of customers signed up")
    # print('\n')
    col_names = [i[0] for i in mycursor.description]

    output = mycursor.fetchall()
    
    print(col_names)
    for i in range(len(output)):
        print(output[i])
    admin_menu()

# Define the remove taxi function
def remove_taxi():
    print("Remove Taxi")
    # Implement remove taxi functionality here
    taxi_no = tuple(input("Enter taxi number(car_no) to remove: ").split())
    mycursor.execute("update taxi set status = NULL where car_no = %s",(taxi_no))
    cnx.commit()
    print(f"Taxi {taxi_no} removed successfully!")
    admin_menu()

# Define the remove driver function
def remove_driver():
    print("Remove Driver")
    driver_id = tuple(input("Enter driver id: ").split())
    mycursor.execute("update driver set status = NULL where id = %s",(driver_id))
    cnx.commit()
    print(f"Driver with id: {driver_id} removed successfully!")
    admin_menu()
def add_taxi():
    print("Add Taxi")
    # Implement add taxi functionality here
    taxi_no = input("Enter taxi number: ")
    model= input("Enter taxi model: ")
    maxpassenger= input("Enter taxi maxpassenger: ")
    registerunder= input("Enter taxi registerunder: ")
    servicedate= input("Enter taxi servicedate: ")
    status= input("Enter taxi status: ")

    mycursor = cnx.cursor()
    sql = "INSERT INTO taxi (car_no, model, max_passengers, registered_under, service_date, status) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (taxi_no, model, maxpassenger, registerunder, servicedate, status)

    # Execute the SQL statement
    mycursor.execute(sql, val)
    cnx.commit()

    print(mycursor.rowcount, "record inserted.")
    
    print("Taxi added successfully!")
    admin_menu()
def add_driver():
    print("Add Driver")
    # Implement add driver functionality here
    driver_firstname = input("enter first name: ")
    driver_lastname = input("Enter last name: ")
    driver_age=input("enter driver age:")
    driver_gener=input("enter driver gender:")
    driver_ratings= input("enter driverratings:")
    driver_status=input("enter driver_status:")
    driver_license=input("enter driver license")
    
    mycursor = cnx.cursor()
    sql = "INSERT INTO driver (fn,ln, age, gender, ratings, status, license) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (driver_firstname, driver_lastname, driver_age, driver_gener, driver_ratings, driver_status, driver_license)

    # Execute the SQL statement
    mycursor.execute(sql, val)
    cnx.commit()

    print(mycursor.rowcount, "record inserted.")
    
    print("Driver added successfully!")
    admin_menu()

# Define the back to main menu function
def back_to_main_menu():
    main_menu()

def login_menu():
    print("Login Menu")
    print("1. Customer login")
    print("2. Driver login")
    print("3. Back to main menu")
    choice = input("Enter your choice: ")
    if choice == "1":
        customer_login()
    elif choice == "2":
        driver_login()
    elif choice == "3":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        login_menu()

def customer_login():
    print("Customer Login")
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Check if username and password are correct
    mycursor.execute("SELECT c_id FROM login WHERE username = %s AND password = %s and c_id is not null", (username, password))
    
    # get the results of the query
    user = mycursor.fetchone()
    
    if user:
        mycursor.execute("SELECT c_id FROM login WHERE username = %s AND password = %s and c_id is not null", (username, password))
        customer = mycursor.fetchone()
        print("Login successful!")
        print(customer)
        customer_menu(customer)
    else:
        print("Invalid username or password. Please try again.")
        customer_login()

# Define the customer menu function
def customer_menu(user):
    print("Customer Menu")
    print("1. Book a ride")
    print("2. Cancel current ride")
    print("3. Check status of current ride")
    print("4. Make payment")
    print("5. View previous rides")
    print("6. Back to main menu")
    choice = input("Enter your choice: ")
    if choice == "1":
        book_ride(user)
    elif choice == "2":
        cancel_ride(user)
    elif choice == "3":
        check_ride_status(user)
    elif choice == "4":
        make_payment(user)
    elif choice == "5":
        viewc_previous_rides(user)
    elif choice == "6":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        customer_menu(user)

# Define the book ride function
def book_ride(user):
    print("Book a ride")
    pickup = int(input("pickup location:"))
    destination =int(input("destination location: "))
    mycursor.execute("select distinct(r.d_id) as available_drivers from rides_data as r join driver on driver.id = r.d_id where (r.status = 'done' or r.status = 'cancel') and driver.status = 0 ")
    
    col_names = [i[0] for i in mycursor.description]

    output = mycursor.fetchall()
    
    print(col_names)
    for i in range(len(output)):
        print(output[i])

    driver = input("enter driver id: ")
    mycursor.execute("select distinct(r.car_no) as taxis from rides_data as r join taxi on taxi.car_no = r.car_no where (r.status = 'done' or r.status = 'cancel') and taxi.status = 0 ")
    col_names = [i[0] for i in mycursor.description]
    output = mycursor.fetchall()
    
    print(col_names)
    for i in range(len(output)):
        print(output[i])
    car = input("enter car number: ")
    status='ongoing'


    dt = datetime.datetime.now()
    quer = "INSERT INTO rides_data (c_id, d_id, car_no, status) VALUES (%s, %s, %s, %s)"

    # create a new row with a primary key
    data = (user[0],driver,car,status)

    # execute the insert statement
    mycursor.execute(quer, data)
    cnx.commit()
    # mycursor.execute("select r.travel_id from rides_data as r join payments as p on r.travel_id = p.travel_id where r.c_id = %s order by r.travel_id desc limit 1",(user))
    mycursor.execute("select travel_id from rides_data where status = 'ongoing' and c_id = %s order by travel_id desc limit 1",(user))
    travel = mycursor.fetchone()
    # Implement book ride functionality here
    mycursor.execute("insert into payments(travel_id,dist,destination,pickup,charges) values(%s,%s,%s,%s,%s)",(travel[0],destination-pickup,destination,pickup,(destination-pickup)*1000))
    cnx.commit()
    customer_menu(user)


# Define the cancel ride function
def cancel_ride(user):
    print("Cancel current ride")
    # Implement cancel ride functionality here
    # print("Cancel ride functionality not implemented yet.")
    mycursor.execute("select r.travel_id from rides_data as r join payments as p on r.travel_id = p.travel_id where r.c_id = %s order by r.travel_id desc limit 1",(user))
    travel = mycursor.fetchone()
    mycursor.execute("update rides_data set status = 'cancel' where travel_id = %s and status = 'ongoing'",(travel))
    cnx.commit()
    print("ride cancelled")
    customer_menu(user)

# Define the check ride status function
def check_ride_status(user):
    print("Check status of current ride")
    # Implement check ride status functionality here
    # print("Check ride status functionality not implemented yet.")
    mycursor.execute("select r.travel_id from rides_data as r join payments as p on r.travel_id = p.travel_id where r.c_id = %s order by r.travel_id desc limit 1",(user))
    travel = mycursor.fetchone()
    mycursor.execute("select r.status from rides_data as r where travel_id = %s",(travel))
    # travel = mycursor.fetchone()
    # mycursor.execute("select r.status from payments as p join rides_data as r on p.travel_id = r.travel_id where r.travel_id = %s",(travel))
    col_names = [i[0] for i in mycursor.description]
    # print('\n')
    output = mycursor.fetchall()
    
    print(col_names)
    for i in range(len(output)):
        print(output[i])
    customer_menu(user)

# Define the make payment function
def make_payment(user):
    # print(user)
    print("Make payment")
    # Implement make payment functionality here
    # print("Make payment functionality not implemented yet.")
    mycursor.execute("select r.travel_id from rides_data as r join payments as p on r.travel_id = p.travel_id where r.c_id = %s order by r.travel_id desc limit 1",(user))
    travel = mycursor.fetchone()
    if(travel):
        mycursor.execute("select p.charges from payments as p join rides_data as r on p.travel_id = r.travel_id where r.travel_id = %s and r.status = 'ongoing'",(travel))
        col_names = [i[0] for i in mycursor.description]
    # print('\n')
        output = mycursor.fetchall()
    
        print(col_names)
        for i in range(len(output)):
            print(output[i])

        mycursor.execute("update rides_data set status = 'done' where travel_id = %s and status = 'ongoing'",(travel))
        cnx.commit()
    else:
        print("No current ride.")
    customer_menu(user)

# Define the view previous rides function
def viewc_previous_rides(user):
    print("Previous rides")
    # Implement view previous rides functionality here
    # print("View previous rides functionality not implemented yet.")
    mycursor.execute("select * from rides_data as r join payments as p on r.travel_id = p.travel_id where r.c_id = %s",(user))
    col_names = [i[0] for i in mycursor.description]
    # print('\n')
    output = mycursor.fetchall()
    
    print(col_names)
    for i in range(len(output)):
        print(output[i])
    customer_menu(user)

# driver login
def driver_login():
    print("Driver Login")
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Implement driver login functionality here
    mycursor.execute("SELECT * FROM login WHERE username = %s AND password = %s", (username, password))
    
    # get the results of the query
    user = mycursor.fetchone()
    
    if user:
        print("Driver login successful.")
        mycursor.execute("SELECT d_id FROM login WHERE username = %s AND password = %s", (username, password))
        driver = mycursor.fetchone()
        driver_menu(driver)
    else:
        print("Invalid username or password. Please try again.")
        driver_login()

def is_valid_driver(username, password):
    # Implement driver authentication logic here
    # Return True if username and password are valid, else False
    return False

def driver_menu(driver):
    print("Driver Menu")
    print("1. View previous rides")
    print("2. Check current ride request")
    print("3. View customer's current location")
    print("4. Back to main menu")
    choice = input("Enter your choice: ")
    if choice == "1":
        view_previous_rides(driver)
    elif choice == "2":
        check_current_ride_request(driver)
    elif choice == "3":
        view_customer_location(driver)
    elif choice == "4":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        driver_menu()

def view_previous_rides(driver):
    print("View previous rides")
    mycursor.execute("select * from rides_data as r join payments as p on r.travel_id = p.travel_id where r.d_id = %s",(driver))
    col_names = [i[0] for i in mycursor.description]
    # print('\n')
    output = mycursor.fetchall()
    
    print(col_names)
    for i in range(len(output)):
        print(output[i])
    # Implement logic to fetch and display driver's previous rides here
    driver_menu(driver)

def check_current_ride_request(driver):
    print("Check current ride request")
    # Implement logic to check if there is any ride request for the driver here
    mycursor.execute("select * from rides_data as r join payments as p on r.travel_id = p.travel_id where r.d_id = %s order by r.travel_id desc limit 1",(driver))
    col_names = [i[0] for i in mycursor.description]
    # print('\n')
    output = mycursor.fetchall()
    
    print(col_names)
    for i in range(len(output)):
        print(output[i])
    
    driver_menu(driver)

def view_customer_location(driver):
    print("View customer's current location")
    # Implement logic to check if there is any ride request for the driver here
    mycursor.execute("select p.pickup , p.destination from rides_data as r join payments as p on r.travel_id = p.travel_id where r.d_id = %s and r.status  = 'ongoing' order by r.travel_id desc limit 1",(driver))
    col_names = [i[0] for i in mycursor.description]
    # print('\n')
    output = mycursor.fetchall()
    
    print(col_names)
    for i in range(len(output)):
        print(output[i])
    # Implement logic to fetch and display customer's current location here
    driver_menu(driver)

cnx = mysql.connector.connect(
  host="localhost",
  user="root",
  password="anmol007",
  database="aaggy"
)

# create a cursor
mycursor = cnx.cursor()
main_menu()
