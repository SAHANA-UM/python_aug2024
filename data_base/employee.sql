use sahana_db;

create table employee(id int primary key auto_increment, name varchar(50) not null, designation varchar(40) not null, technology varchar(30) not null, phone_num bigint unique, commission int, salary float default 0, year_of_exp int);

insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('sahana', 'manager', 'python', '123', '10', '140000', 3);
insert into employee(name, designation, technology, phone_num, commission, salary) values('sonali', 'team leader', 'java', '1122334455', '15', '25000');
insert into employee(name, designation, technology, phone_num, salary, year_of_exp) values('zoro', 'developer', 'c++','1000000007', '50000', 5);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('taran', 'web designer', 'html', '1425367890', '50', '25000', 8);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('karan', 'digital designer', 'wed designing', '5522441133', '10000', '25000', 3);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('varun', 'chief manager', 'python', '1472583698','5', '250000', 7);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('spoorti', 'designer', 'java', '8855667744', '10000', '25000', 3);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('sanjana', 'developer', 'c', '4455667788', '50', '20000', 6);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('shreya', '', 'python', '4455667708','10000', '25000', 3);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('shakuntala', 'manager', 'c', '9955884577', '3', '250000', 10);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('roshini', 'manager', 'java', '3366998855', '10', '500000', 6);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('rohini', 'manager', 'python', '3366998005', '10000', '25000', 3);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('sam', 'teamleader', 'java script', '2583690070', '10', '25000', 4);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('samruddhi', 'manager', 'python', '2583691490','10000', '25000', 3);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('samruddh', 'manager', 'python','2583001470','10000', '25000', 3);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('rohit', 'manager', 'python', '1200559932', '10000', '25000', 3);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('pratibha', 'developer', 'python','1200550432', '52', '250000', 12);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('kumar', 'teamleader', 'c', '5577330014', '22', '150000', 5);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('umma', 'manager', 'java', '5578330014','19', '21000', 5);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('rajani', 'manager', 'c++','5576630014', '25', '250000', 8);
insert into employee(name, designation, technology, phone_num, commission, salary, year_of_exp) values('rajeev', 'teamleader', 'python', '5552330014','18', '50000', 4);

select * from employee; 

select salary from employee;

update employee
set salary =100000
where id = 14;

select id = 14 from employee; 
