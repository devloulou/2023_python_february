/*
 * lead, lag
 * 
 * analitikus függvények
 * */

select * from employees_hrschema eh;

select * from departments_hrschema dh;

create table emp_test (
id serial, 
name varchar(50),
position_name varchar(100),
active boolean,
start_date date,
end_date date
);

delete from emp_test;

insert into emp_test(id, name, position_name, active, start_date)
values (1, 'Bill Gates', 'Developer', true, date'1989-01-20');

insert into emp_test(id, name, position_name, active, start_date)
values (1, 'Bill Gates', 'Lead Developer', true, date'1994-01-20');

insert into emp_test(id, name, position_name, active, start_date)
values (1, 'Bill Gates', 'Developement Manager', true, date'2004-01-20');


insert into emp_test(id, name, position_name, active, start_date)
values (2, 'Elon Musk', 'Frontend', true, date'1989-01-20');

insert into emp_test(id, name, position_name, active, start_date)
values (2, 'Elon Musk', 'Backend', true, date'1994-01-20');

insert into emp_test(id, name, position_name, active, start_date)
values (2, 'Elon Musk', 'Team Lead', true, date'2004-01-20');


select * from emp_test;

select
	count(t.position_name)over(partition by id,
	name
order by
	start_date asc,
	active desc) as pre_position,
	lead(t.position_name)over(partition by id,
	name
order by
	start_date asc) as next_position,
	sum(t.id)over(partition by id
order by
	active),
	*
	--sum(t.id), id
from
	emp_test t
--group by id
;

/*
 * subselect - subquery
 * with 
 * 
 * 
 * */
select
	employee_id,
	last_name
from
	(
	select
		*
	from
		(
		select
			*
		from
			employees_hrschema eh
		where
			eh.department_id >= 4) as t) as t1;

/*
 * with - 1. performancia optimalizálást: with materializációt 
 * 		- 2. ad egy átláthatóbb, bővíthetőbb struktúrát
 * 
 * */

with base_data as (
select
	*
from
	emp_test t
where
	t.id = 1
), 
agg_data as (
select
	lead(bd.position_name)over(
	order by start_date),
	*
from
	base_data bd
)
select
	*
from
	agg_data;


/*
 * string függvények
 * 
 * */
-- dual table - beépített dummy tábla

---substring függvény
-- position
select 
substring(str_1, position('alma' in str_1), 4) as sbtr,
position('alma' in str_1) as p_str,
replace(str_1, 'alm', '111')
from (
select 'almásrétesalmafa' as str_1,
'indul a görög aludni' as str_2
) as t

;
-- like -os keresést
-- _ egy karakteret helyettesít be
-- % bármilyen és bármennyi karakter helyettesítése

select * from ( 
select 'almásrétesalmafa' as str_1,
'indul a görög aludni' as str_2,
'alma' as str_3
) as t
where t.str_2 like '%a%'
;

/*
 * string concatenation - stringek összefűzése
 * */
select
a || ' ' || b, -- concatenation with operator,
concat(a,' ', b)
from (
select 'Karcsi' as a, 'Vezet' as b
) t

--- to_char()

select
to_char(datum, 'ww'),
datum,
to_char(mynum, '999,999,999') as my_num,
mynum
from (
select now() as datum,
900000000 as mynum
) as t
;

/*
 * datum függvények
 *  
 * dátummá alakít egy nem dátum típust - stringet
 * dátum típusú adattal különböző műveletek
 * */

select
date'2022-12-30',
to_date(to_char(my_t, '99999999'), 'YYYYMMDD'),
today + interval'12 month',
today - interval'1 year',
extract(week from today)
from (
select now() as today, 20221230 as my_t, '2022-12-30' as my_t1) as t
;


select CURRENT_DATE;
select CURRENT_TIME;
select CURRENT_TIMESTAMP, now();

SELECT DATE_TRUNC('month', current_timestamp)
