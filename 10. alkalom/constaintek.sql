/*
 * 
 * serial type - auto increment adattípus
 * 1
 * Adatmodellezés - 3rd Normal Form
 * 
 * 3 lépcsője van
 * Data modelling: ER diagram - Entity Relationship diagram
 * Conceptual: az elképzelt kapcsolatot vázolod fel a táblák között
 * Logical - logikai adatmodellezés: a felvázolt tábláknál megjelöli hogy milyen mezők
 * milyen adattípussal szerepelnek a táblákban
 * és megjelöljük a táblák közötti kapcsolatot
 * Physical - fizikai adatmodell: adatbázisra specifikált adamodell megfeleltetés
 * ezek a create scriptek
 * 
 * Táblák ID mező:
 * rekord - az egy sorban lévő logikailag összetartozó adat
 * az ID az a rekord egyértelmű azonosítására szolgál, egyedi azonosító
 * 
 * Az ID általában egy generált azonosító, 
 * ha nem generált azonosítót használunk, akkor természetes kulcsokkal dolgozunk
 * 
 * 
 * Kapcsolat táblák között:
 * szülő - gyermek kapcsolat - 
 * 
 * ahhoz, hogy szülő - gyermek kapcsolatot alakítsak ki
 * szükség van a szülő táblában primary key-ekre - elsődleges kulcsra
 * a gyermek táblában pedig foreign key-re - vagy idegen kulcsra
 * 
 * Primary key: a táblában unique értéknek kell lennie és nem lehet null értéke
 * 
 * Constraintek - Megszorítások
 * Primary key - 
 * 				- unique - egyedi
 * 				- not null - a mező értéke nem lehet üres - nem lehet null
 * foreign key constraint
 * check constraint - db > 1
 * */

/*
 * 3 tábla
 * employee
 * positions
 * hiring
 * */

create table employee (
id serial,
name text,
salary integer,
birth_date date,
position_id integer,
hiring_id integer
);

create table hiring (
id serial,
start_date date,
status boolean
);

create table positions(
id serial,
job text,
leader text,
department text
);

drop table test_departments;

create table test_departments (
id serial,
department_name varchar(10)
);

select * from test_departments;

insert into test_departments (id, department_name)
values (1, 'IT');



select * from hiring;
select * from positions;
select * from employee;

delete from employee where id = 2;

insert into hiring (start_date, status) 
values (to_date('1990.09.16.', 'YYYY.MM.DD.'), true);


insert into hiring (start_date, status) 
values (to_date('1980.09.16.', 'YYYY.MM.DD.'), true);


insert into positions(job, leader, department)
values ('Data Engineer', 'Mekk Elek', 'IT');

insert into positions(job, leader, department)
values ('Data Engineer', 'Mekk Elek', 'IT');

name text,
salary integer,
birth_date date,
position_id integer,
hiring_id integer

insert into employee (name, salary, birth_date, position_id, hiring_id)
values ('Kovács Ricsi', 10000, to_date('1990.09.16.', 'YYYY.MM.DD.'),
1, 1);

/* Inkonzisztens állapot
 * */
insert into employee (name, salary, birth_date, position_id, hiring_id)
values ('Wasabi István2', null, to_date('1980.09.16.', 'YYYY.MM.DD.'),
2, 2);



/*
 * SQL - select statement
 * 
 * adatok lekérdezése és formázása
 * 
 * select mezok_oszlopok, mezo2, mezo3 from 
 * select * from - minden oszlop, ami a táblában van
 * 
 * tábla és mező alias
 * 
 * */

select position_id as a, name, id from employee e;

select e.id , e."name" , e.salary as "Havi Fizetés"  from employee e;

--- filterezés / szűrés - where feltétel
--- and - or
select * from employee e 
where id = 1 and name = 'Kovács Risi';

select * from employee e 
--where id <> 1;
where id != 1;

--- null value
select * from employee e 
where e.salary is not null

/*
 * group by
 * having
 * order by 
 * limit
 * 
 * sql kiértékelési sorrendje
 * 
 * feladatot -> aggregációt, analitikus függvényeket,
 * delete, insert, update
 * 
 * */

