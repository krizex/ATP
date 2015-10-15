create database atp;

use atp;

create table FLIGHT_INFO(
id int NOT NULL AUTO_INCREMENT,
query_date date,
query_time time,
flight_date date,
flight_number char(32),
dep_time time,
dep_airport char(64),
arr_time time,
arr_airport char(64),
elapsed_time char(32),
punctuality_rate char(32),
delay_time char(32),
ticket_price int,
PRIMARY KEY (id)
);


create table FLIGHT_LOWEST_PRICE_INFO(
id int NOT NULL AUTO_INCREMENT,
query_date date,
query_time time,
dep_code char(8),
arr_code char(8),
flight_date date,
flight_number char(32),
dep_time time,
arr_time time,
carrier char(128),
vendor_name char(128),
ticket_price int,
PRIMARY KEY (id)
);
