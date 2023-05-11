delimiter //
create trigger check_driver before insert
on rides_data
for each row
begin 
if exists (select * from driver where driver.id = new.d_id and status = 1) then
	SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Driver is already on another ride';
end if;
end;
//

delimiter //
create trigger driver_status before update
on rides_data
for each row
begin
if old.status = 'ongoing' and new.status = 'done' then
	update driver set status = 0 where id = new.d_id;
elseif old.status = 'ongoing' and new.status = 'cancel' then
	update driver set status = 0 where id = new.d_id;
end if;
end;
//