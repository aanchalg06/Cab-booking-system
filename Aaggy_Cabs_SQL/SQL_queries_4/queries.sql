select count(*) as rides_by_Henry from rides_data where c_id = (select id from customer where fn = "Henry" and ln ="Cello" );
select * from driver where ratings=5 and rides_done>=10;
select * from taxi where status = 0 and max_passengers = 5;
update driver set age = 25 where age<27;
update rides_data set status = "cancel" where travel_id = 120;
select rides_data.c_id,customer.fn,customer.gender,count(*) as rides from rides_data inner join customer on rides_data.c_id = customer.id group by c_id ; 
select rides_data.car_no,taxi.model,count(*) as rides from rides_data inner join taxi on taxi.car_no = rides_data.car_no group by car_no limit 3 ;
select sum(payments.charges) from payments natural join rides_data where rides_data.date_time between "2022-01-01 00:00:00 "and "2022-12-31 23:59:59";
select payments.pickup , count(*) as num_pickups from rides_data inner join payments on payments.travel_id = rides_data.travel_id group by pickup limit 5;
select count(*) as rides_cancelled from rides_data where status = "cancel";
select car_no,service_date from taxi where service_date = (select min(service_date) from taxi);
update taxi set service_date = "2023-02-17" where car_no = "H2-94";
