from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'aaggy2'

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="anmol007",
    database="aaggy2"
)

query=["select count(*) as rides_done from rides_data where c_id = (select id from customer where fn = %s and ln =%s)",
       "select * from driver where ratings=5 and rides_done>=10",
       "select * from taxi where status = 0 and max_passengers = 5",
       "update rides_data set status = \"cancel\" where travel_id = 120",
       "select rides_data.c_id,customer.fn,customer.gender,count(*) as rides from rides_data inner join customer on rides_data.c_id = customer.id group by c_id ",
       "select payments.pickup , count(*) as num_pickups from rides_data inner join payments on payments.travel_id = rides_data.travel_id group by pickup order by num_pickups desc limit 5",
       "select count(*) as rides_cancelled from rides_data where status = \"cancel\"",
       "select car_no,service_date from taxi where service_date = (select min(service_date) from taxi)",
       "update rides_data set status = 'done' where travel_id =4",
       "insert into rides_data(c_id,d_id,car_no,date_time,status) values (2,2,\"AD-63\",'2022-04-23 15:25:43','ongoing');"]
# //query 1
print('#'*100)
print('Query 1\n')

print('Enter first name of customer: ')
firstname= input()
# print('\n')
print('Enter last name of customer: ')
lastname=input()
# print('\n')

# print("select count(*) as rides_by_Henry from rides_data where c_id = (select id from customer where fn = %s and ln =%s", firstname,lastname)

cursors = cnx.cursor()
query1=query[0]
info=(firstname,lastname)
cursors.execute(query1,info)
output = cursors.fetchall()
# x=str(output[0][0])

print('Count of rides done = ', output[0][0])
# print((output[0][0]))
print('\n')
# print('\n')



# query2
print('#'*100)
print('Query 2')
print('\n')
print(query[1])
print('\n')

print('show drivers with ratings 5 and experience of more than 10 rides ')
cursors = cnx.cursor()
cursors.execute(query[1])
output = cursors.fetchall()

for i in range(len(output)):
    print(output[i])

print('\n')

# print('\n')

# query 3
print('#'*100)
print('Query 3')
print('\n')

print("show taxis available and capacity of 5 seats")
print('\n')
cursors = cnx.cursor()
cursors.execute(query[2])
output = cursors.fetchall()

for i in range(len(output)):
    print(output[i])


# query 4
print('#'*100)
print('Query 4')
print('\n')

print("cancel the ride with travel id 120")
print('\n')
cursors = cnx.cursor()
cursors.execute(query[3])
cnx.commit()
output = cursors.fetchall()

for i in range(len(output)):
    print(output[i])

# query 5
print('#'*100)
print('Query 5')
print('\n')

print("data of customers along with rides they travelled")
print('\n')
cursors = cnx.cursor()
cursors.execute(query[4])
output = cursors.fetchall()

for i in range(len(output)):
    print(output[i])


# query 6
print('#'*100)
print('Query 6')
print('\n')

print("top 5 pickup locations")
print('\n')
cursors = cnx.cursor()
cursors.execute(query[5])
output = cursors.fetchall()

for i in range(len(output)):
    print(output[i])


# query 7
print('#'*100)
print('Query 7')
print('\n')

print("total number of rides cancelled")
print('\n')
cursors = cnx.cursor()
cursors.execute(query[6])
output = cursors.fetchall()

for i in range(len(output)):
    print(output[i])

# query 8
print('#'*100)
print('Query 8')
print('\n')

print("taxi with the oldest service date")
print('\n')
cursors = cnx.cursor()
cursors.execute(query[7])
output = cursors.fetchall()

for i in range(len(output)):
    print(output[i])

# query 9
print('#'*100)
print('Query 9')
print('\n')

print("updating rides status")
print('\n')
cursors = cnx.cursor()
cursors.execute(query[8])
cnx.commit()
output = cursors.fetchall()

for i in range(len(output)):
    print(output[i])

# query 10
print('#'*100)
print('Query 10')
print('\n')

print("inserting rides ")
print('\n')
cursors = cnx.cursor()
cursors.execute(query[9])
output = cursors.fetchall()

for i in range(len(output)):
    print(output[i])

