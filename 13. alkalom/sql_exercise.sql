/*
 * Csináljunk egy olyan kimutatást
 * ami tartalmazza a következőket:
 * 
 * melyik dolgozó, mennyit keres és milyen divízióban dolgozik
 * és ki a divízió vezetője
 *
 * help:
 * van e az adatbázisnak meta adat leírása
 * 
 * honnan tudom, hogy 2 táblát hogyan kell joinolni
 * rossz hír:
 * vannak olyan táblák, ahol nincs kialakítva szülő-gyermek kapcsolat és megis
 * össze tudod kapcsolni valamilyen tranformáció segítségével
 * 
 * xxxxxxxx-xxxxxxxx-xxxxxxxx
 * xxxxxxxx
 * 
 * jó hír:
 * ha van kapcsolat a táblák között, akkor azt egyszerűen meg tudom nézni
 **/

/*
 *  Csináljunk egy olyan kimutatást
 * ami tartalmazza a következőket:
 * 
 * melyik dolgozó, mennyit keres és milyen divízióban dolgozik
 * és ki a divízió vezetője
 * 
 * */

select * from countries_hrschema ch ;
select * from departments_hrschema dh;
select * from dependents_hrschema dh ;
select * from employees_hrschema eh ;
select * from jobs_hrschema jh ;
select * from locations_hrschema lh ;
select * from regions_hrschema rh ;


select
	eh.employee_id,
	eh.first_name || ' ' || eh.last_name as full_name,
	eh.salary,
	dh.department_name,
	eh.manager_id,
	eh2.first_name || ' ' || eh2.last_name as leader_name
from
	employees_hrschema eh
inner join departments_hrschema dh on
	eh.department_id = dh.department_id
left join employees_hrschema eh2 on
	eh.manager_id = eh2.employee_id 
;



select * from countries_hrschema ch ;
select * from departments_hrschema dh;
select * from dependents_hrschema dh ;
select * from employees_hrschema eh ;
select * from jobs_hrschema jh ;
select * from locations_hrschema lh ;
select * from regions_hrschema rh ;


/*
 * Selectáld le nekem a top 3 legtöbb kiadással járó
 * departmentet
 * 
 * */
select
sum(eh.salary) , department_id 
from employees_hrschema eh
group by eh.department_id
order by sum(eh.salary) desc
--order by 1 desc
limit 3;

-- analitikus függvényekkel: over(partition by order by)
select
distinct
sum(eh.salary)over(partition by eh.department_id) as kiadas,
eh.department_id
from employees_hrschema eh
order by kiadas desc
limit 3


select * from employees_hrschema eh ;

/*
 * Készítsetek egy olyan kimutatást, 
 * amely tartalmazza a következő adatokat:
 * 
 * Dolgozó teljes neve, email cím első fele - a @ előtti rész - , 
 * mi a dolgozó foglalkozása
 * ki a vezetője, a vezető és a beosztott fizetése közötti különbség
 * 
 * és csak azok a dolgozók legyenek benne a leválogatásban
 * akik 5000 -nél többet keresnek és 94 után csatlakoztak a céghez
 * 
 * where feltétel:  
 * kik 5000 -nél többet keresnek és 
 * 94 után csatlakoztak a céghez
 * */

select * from countries_hrschema ch ;
select * from departments_hrschema dh;
select * from dependents_hrschema dh ;
select * from employees_hrschema eh ;
select * from jobs_hrschema jh ;
select * from locations_hrschema lh ;
select * from regions_hrschema rh ;


/*
 * Dolgozó teljes neve, email cím első fele - a @ előtti rész - , 
 * mi a dolgozó foglalkozása
 * ki a vezetője, a vezető és a beosztott fizetése közötti különbség*/

select
	eh.first_name || ' ' || eh.last_name as full_name,
	replace(eh.email, '@sqltutorial.org', '') as nickname,
	substring(eh.email, 0, position('@' in eh.email)) as nick_name,
	jh.job_title,
	eh2.first_name || ' ' || eh2.last_name as leader_name,
	eh2.salary - eh.salary as salary_diff
from
	employees_hrschema eh
inner join jobs_hrschema jh on
	eh.job_id = jh.job_id
left join employees_hrschema eh2 on
	eh.manager_id = eh2.employee_id
where
	eh.salary > 5000
	and eh.hire_date > date'1994-01-01';

