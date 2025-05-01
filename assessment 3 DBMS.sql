create table Bank
(
branch_id int unique not null,
branch_name varchar(100) not null,
branch_city varchar(100) not null
);

insert into bank values (1001,'Gota Branch','Ahmedabad');
insert into bank values (1002,'Iskon Branch','Ahmedabad');
insert into bank values (1003,'Parimal Garden Branch','Ahmedabad');
insert into bank values (1004,'Univercity Road Branch','Rajkot');
insert into bank values (1005,'Keshod Branch','Keshod');

select * from bank;

create table Account_Holder
(
account_holder_id int primary key,
account_no int unique not null,
account_holder_name varchar(100) not null,
city varchar(100) not null,
contact double unique not null,
date_of_account_create date not null,
account_status varchar(12) not null, -- 'active' or 'terminated'
account_type varchar(15) not null,
balance double not null
);

insert into account_holder values (1,100012345,'Parth Vadariya','Rajkot',9714013578,'1999-01-19','Active','Saving',100000);
insert into account_holder values (2,100012335,'Deep Patel','Ahmedabad',6353940646,'2001-05-25','Active','Saving',90000);
insert into account_holder values (3,100012325,'Pranshu Patel','Ahmedabad',9687343468,'2005-11-25','Active','Saving',10000);
insert into account_holder values (4,100012315,'Dev Panchal','Keshod',9429412538,'2002-12-10','Active','Saving',50000);
insert into account_holder values (5,100012305,'Mrugal Patel','Ahmedabad',7016672877,'2000-09-20','Active','Saving',25000);

select * from Account_Holder;

create table Loan_Table
(
loan_no int primary key,
branch_id int not null,
account_holder_id int not null,
loan_amount double not null,
loan_type varchar(15) not null,
foreign key loan_table(account_holder_id) references Account_Holder(account_holder_id)
);

insert into loan_table values (123654789,1002,5,100000,'House Loan');
insert into loan_table values (102365478,1001,3,1000000,'Morgadge Loan');
insert into loan_table values (109876542,1005,4,500000,'Car Loan');

select * from Loan_Table;

-- Make sure after the transaction the account information have to be updated for both the credit account and the debited account

update account_holder set balance = balance - 50000 where account_no = 100012345;
update account_holder set balance = balance + 50000 where account_no = 100012325;
select * from Account_Holder;

-- Also fetch the details of the account holder who are related from the same city 

select * from account_holder where city = 'ahmedabad';

-- Write a query to fetch account number and account holder name, whose accounts were created after 15th of any month

select account_no,account_holder_name from account_holder where day (date_of_account_create) >15;

-- Write a query to display the city name and count the branches in that city. Give the count of branches an alias name of Count_Branch.

select branch_city,count(branch_id) as count_branch from bank group by branch_city; 

-- Write a query to display the account holder’s id, account holder’s name,branch id, and loan amount for people who have taken loans. (NOTE : use sql join concept to solve the query)

select account_holder.account_holder_id,account_holder.account_holder_name,loan_table.branch_id,loan_table.loan_amount 
from account_holder join loan_table on account_holder.account_holder_id = loan_table.account_holder_id; 