-- Number of queries made every hour
Select date_format(date_time , '%Y-%m-%d %H') as booking_hourly , count(*) from rides_data group by booking_hourly with rollup;

-- Revenue by Location
Select pickup,sum(payments.charges) as revenue from payments group by pickup with rollup;

-- Bookings by Month
Select date_format(rides_data.date_time, '%Y %m') as Months , count(*) as bookings_count , sum(payments.charges) as revenue from rides_data join payments on rides_data.travel_id = payments.travel_id group by Months ;

-- Revenue by Cab type
Select taxi.model as cab_type , sum(payments.charges) from payments join (rides_data inner join taxi on rides_data.car_no = taxi.car_no) on rides_data.travel_id = payments.travel_id group by cab_type with rollup;

-- Customer's accepted or rejected rides
select customer.fn , rides_data.status , count(*) as rides from rides_data join customer on customer.id = rides_data.c_id group by customer.fn , rides_data.status with rollup;

-- Cabs with their status count
select taxi.model , rides_data.status ,count(*) as count from rides_data , taxi where rides_data.car_no = taxi.car_no group by taxi.model , rides_data.status with rollup order by field( rides_data.status,"cancel","ongoing","done") desc , count;

-- customer loyality month wise
select month(date_time) as booking_month , count(distinct c_id)/count(*) as customer_loyality from rides_data group by booking_month with rollup;

-- average revenue of two car model by months
select month(r.date_time) as booking_month , sum(case when t.model = 'mx-6' then 1 else 0 end) as mx6_bookings , sum(case when t.model = 'sentra' then 1 else 0 end) as sentra_booking from rides_data as r join taxi as t on r.car_no = t.car_no group by booking_month with rollup;