/*categories							
Category_ID	category_name	category_description	created_date	last_modified_date	modified_user	created_user	
1	PC						
							
product							
product_id	product_name	price	product_description	created_date	created_user	last_modified_date	modified_user
1	Lenovo						
							
category_product_map							
product_map_id	category_id	product_id					
1	1	1					
							
stocks							
product_map_id	cnt	created_date	modified_date				
*/
drop table categories_webshop;
create table categories_webshop(
category_id serial primary key,
category_name varchar(20),
category_description text,
created_date date default now(),
created_user varchar(50),
modified_date date,
modified_user varchar(50)
);


create table product_webshop(
product_id serial primary key,
product_name varchar(50),
price int,
product_description text,
created_date date default now(),
created_user varchar(50),
modified_date date,
modified_user varchar(50)
);

create table category_product_map_webshop(
product_map_id serial primary key,
category_id int,
product_id int,
CONSTRAINT category_id_webshop_fk
FOREIGN KEY (category_id) REFERENCES public.categories_webshop(category_id)
ON DELETE CASCADE ON UPDATE cascade,
CONSTRAINT product_id_webshop_fk
FOREIGN KEY (product_id) REFERENCES public.product_webshop(product_id)
ON DELETE CASCADE ON UPDATE cascade
)
;


create table stock_webshop (
product_map_id int,
cnt int,
created_date date default now(),
modified_date date,
CONSTRAINT product_map_fk
FOREIGN KEY (product_map_id) REFERENCES public.category_product_map_webshop(product_map_id)
ON DELETE CASCADE ON UPDATE cascade
);

-- indexek, index stratégia, pro - kontra

select * from categories_webshop;
select * from product_webshop;
select * from category_product_map_webshop;
select * from stock_webshop;


insert into categories_webshop (category_name,category_description,created_user) values ('Videókártya','Ez egy teszt','ricsi');
insert into categories_webshop (category_name,category_description,created_user) values ('Processzor','Ez egy teszt','ricsi');
insert into categories_webshop (category_name,category_description,created_user) values ('Monitor','Ez egy teszt','ricsi');
insert into categories_webshop (category_name,category_description,created_user) values ('Egér','Ez egy teszt','ricsi');
insert into categories_webshop (category_name,category_description,created_user) values ('Kiegészítők','Ez egy teszt','ricsi');
insert into categories_webshop (category_name,category_description,created_user) values ('Tápegység','Ez egy teszt','ricsi');



insert into product_webshop (product_name,price,created_user) values ('LG 123','300','ricsi');
insert into product_webshop (product_name,price,created_user) values ('NVIDIA 3070','400','ricsi');
insert into product_webshop (product_name,price,created_user) values ('NVIDIA 3070 ti','1320','ricsi');
insert into product_webshop (product_name,price,created_user) values ('NVIDIA 3060','3525','ricsi');
insert into product_webshop (product_name,price,created_user) values ('NVIDIA 3060 Ti','1251','ricsi');
insert into product_webshop (product_name,price,created_user) values ('Valamilyen egér','124','ricsi');
insert into product_webshop (product_name,price,created_user) values ('Razor','1352','ricsi');
insert into product_webshop (product_name,price,created_user) values ('AMD Ryzen 5','1235','ricsi');
insert into product_webshop (product_name,price,created_user) values ('AMD Ryzen 7','23626','ricsi');
insert into product_webshop (product_name,price,created_user) values ('AMD Ryzen 9','26236','ricsi');
insert into product_webshop (product_name,price,created_user) values ('Intel I7','1212','ricsi');
insert into product_webshop (product_name,price,created_user) values ('Intel i5','2356265','ricsi');
insert into product_webshop (product_name,price,created_user) values ('Intel i9','236236','ricsi');
insert into product_webshop (product_name,price,created_user) values ('FSP arany','235235','ricsi');
insert into product_webshop (product_name,price,created_user) values ('Corair arany','23626','ricsi');
insert into product_webshop (product_name,price,created_user) values ('USB stick','23626','ricsi');
insert into product_webshop (product_name,price,created_user) values ('DVD','2','ricsi');


insert into category_product_map_webshop (category_id,product_id) values (3,1);
insert into category_product_map_webshop (category_id,product_id) values (1,2);
insert into category_product_map_webshop (category_id,product_id) values (1,3);
insert into category_product_map_webshop (category_id,product_id) values (1,4);
insert into category_product_map_webshop (category_id,product_id) values (1,5);
insert into category_product_map_webshop (category_id,product_id) values (4,6);
insert into category_product_map_webshop (category_id,product_id) values (4,7);
insert into category_product_map_webshop (category_id,product_id) values (2,8);
insert into category_product_map_webshop (category_id,product_id) values (2,9);
insert into category_product_map_webshop (category_id,product_id) values (2,10);
insert into category_product_map_webshop (category_id,product_id) values (2,11);
insert into category_product_map_webshop (category_id,product_id) values (2,12);
insert into category_product_map_webshop (category_id,product_id) values (2,13);
insert into category_product_map_webshop (category_id,product_id) values (6,14);
insert into category_product_map_webshop (category_id,product_id) values (6,15);
insert into category_product_map_webshop (category_id,product_id) values (5,16);
insert into category_product_map_webshop (category_id,product_id) values (5,17);


insert into stock_webshop (product_map_id,cnt) values (1,30);
insert into stock_webshop (product_map_id,cnt) values (2,40);
insert into stock_webshop (product_map_id,cnt) values (3,512);
insert into stock_webshop (product_map_id,cnt) values (4,235);
insert into stock_webshop (product_map_id,cnt) values (5,623);
insert into stock_webshop (product_map_id,cnt) values (6,34);
insert into stock_webshop (product_map_id,cnt) values (7,2134);
insert into stock_webshop (product_map_id,cnt) values (8,63);
insert into stock_webshop (product_map_id,cnt) values (9,1);
insert into stock_webshop (product_map_id,cnt) values (10,23);
insert into stock_webshop (product_map_id,cnt) values (11,3473);
insert into stock_webshop (product_map_id,cnt) values (12,23);
insert into stock_webshop (product_map_id,cnt) values (13,236);
insert into stock_webshop (product_map_id,cnt) values (14,346);
insert into stock_webshop (product_map_id,cnt) values (15,2135);
insert into stock_webshop (product_map_id,cnt) values (16,46);
insert into stock_webshop (product_map_id,cnt) values (17,37);


create table stock_webshop_test as (
select *from stock_webshop where 1 = 2)
;

select *from stock_webshop_test


insert into stock_webshop_test (product_map_id, cnt)
select product_map_id, cnt from stock_webshop t
where t.product_map_id < 16
;

select *from stock_webshop_test