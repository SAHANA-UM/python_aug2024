 create table IF NOT EXISTS persons(id int primary key auto_increment, name varchar(50) not null, gender varchar(2), location varchar(50), age int check(age > 0));
 
insert into persons(name, gender, location, age) values('Sahana', 'f', 'Dharwad', '20');
insert into persons(name, location, age) values('Reetu', 'Hubbli', '40');
insert into persons(name, gender, location) values('Ram', 'm', 'Dharwad');
insert into persons(name, gender, location, age) values('Sanjana', 'f', 'Mysuru', '10');
insert into persons(name, gender, location, age) values('Rohan', 'm', 'Banglore', '25');
insert into persons(name, gender, location, age) values('Tanu', 'f', 'Dheli', '15');
insert into persons(name, gender, location, age) values('Rina', 'f', 'Belgavi', '80');
insert into persons(name, gender, location, age) values('Uday', 'm', 'Goa', '58');
insert into persons(name, location) values('Sahana', 'Dharwad');
insert into persons(name) values('Roshini');
insert into persons(name, age) values('Tushar','66');
insert into persons(name) values('Spoorti' );
insert into persons(name, gender) values('Pratibha', 'f');
insert into persons(name, gender, age) values('Samruddh', 'm','18');
insert into persons(name, lcation, age) values('Pujara','Patna', '70');
insert into persons(name, gender, age) values('Sam', 'm', '20');
insert into persons(name) values('Shreya');
insert into persons(name, gender, location, age) values('Taran', 'm', 'J&K', '86');
insert into persons(name, gender, location, age) values('Varun', 'm', 'Bagalkoti', '55');
insert into persons(name, gender, location, age) values('Tejas', 'm', 'Dharwad', '15');
insert into persons(name, gender, location, age) values('Sanju', 'f', 'Dharwad', '80');

select * from persons;
select name, location from persons;
select location from persons;
select distinct location from persons;
select * from persons where age < 50;
select * from persons where location = 'Dharwad';

insert into persons(name, gender, location, age) values('Sanju', 'f', 'Dharwad', '50');

select * from persons where age between 20 and 50;
select * from persons where name like 'S%';
select * from persons where name like 'S%a';
select * from persons where name like 'S____a';
select * from persons where name like 'S%';

select * from persons where location in('Hubbli', 'Dharwad', 'Belgavi');

select * from persons where location='Hubbli' or location='Dharwad' or location='Belgavi';

