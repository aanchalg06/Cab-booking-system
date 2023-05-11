-- count rides by customer named "Henry Cello" 
select count(*) as rides_by_Henry from rides_data where c_id = (select id from customer where fn = "Henry" and ln ="Cello" );

-- show drivers with ratings 5 and experience of more than 10 rides 
select * from driver where ratings=5 and rides_done>=10;

-- show taxis available and capacity of 5 seats 
select * from taxi where status = 0 and max_passengers = 5;

-- cancel the ride with travel id 120
update rides_data set status = "cancel" where travel_id = 120;

-- data of customers along with rides they travelled
select rides_data.c_id,customer.fn,customer.gender,count(*) as rides from rides_data inner join customer on rides_data.c_id = customer.id group by c_id ; 

-- top 5 pickup locations
select payments.pickup , count(*) as num_pickups from rides_data inner join payments on payments.travel_id = rides_data.travel_id group by pickup order by num_pickups desc limit 5;

-- total number of rides cancelled
select count(*) as rides_cancelled from rides_data where status = "cancel";

-- taxi with the oldest service date
select car_no,service_date from taxi where service_date = (select min(service_date) from taxi);

-- updating rides change driver status trigger test
update rides_data set status = 'done' where travel_id =4

-- insert rides check driver trigger test
insert into rides_data(c_id,d_id,car_no,date_time,status) values (2,2,"AD-63",'2022-04-23 15:25:43','ongoing');