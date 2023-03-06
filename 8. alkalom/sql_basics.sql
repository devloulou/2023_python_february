-- select 10
/*
 * PostgreSQL - RDBMS - Relational Database Management System - 
 * relációs adatbázisnak
 * SQL - lekérdező nyelv, Structured Query Language
 *  
 * OLTP - OLAP
 * 
 * OLTP - Online Transactional Processing - A kurzus során OLTP-zni fogunk
 * OLAP - Online Analitical Processing - adattárház - DWH - Data WareHouse
 * 
 * modellezési technika függ attól, hogy OLTP vagy OLAP rendszerben dolgozom
 * 
 * OLTP - normal forms, 3nd normal form mint modellezési forma
 * OLAP - dimenzionális modellezés, csillagséma,hópehelyséma, Data Vault
 * 
 * OLTP: "tranzakciós rendszerek", ahol a felhasználó adataival kapcsolatban
 * végzek műveletet: pl előfizetek egy szolgáltatásra,
 * utalok, foglalok egy repjegyet; atomi tranzakció - kicsi dolgokat
 * 
 * OLAP: amikor nagy volumenű és mennyiségű adatot akarsz elemezni
 * 
 * OLTP: Online Transactional Processing 
 * netbank, webshop, akármilyen fizetési rendszer, főkönyvi rendszer, 
 * minden olyan fejlesztés
 * ahol a cél 1 ügyfélhez tartozó adat létrehozás, módositás, törlés: (általában a web applikációk)
 * -> kevés adat használatára
 * -> általában az adat aktuális állapotát tartalmazza
 * 
 * 
 * OLAP: Online Analitical Processing
 * Adattárház, Data Lake, Lakehouse
 * Elemzésre, riportlására és előrejelzésre -> 
 * -> nagy adat elemzésre, aggregációk futtatására
 * Business Intelligence osztályokon lévő üzleti folyamatok
 * -> idősorosan (általában) tartalmazza az elvégzett módositásokat
 * 
 * 
 * * 
 * NoSQL - 
 * 
 * SQL
 * DDL - Data Definition Language
 * create, drop, alter, truncate, comment, rename
 * 
 * DML - Data Manupulation Language
 * insert, update, delete, lock, call, explain plan
 * 
 * DCL - Data Control Language
 * grant, revoke
 * 
 * DQL - Data Query Language
 * select 
 * 
 * */

-- create table
/*
 * create object_típusa object_neve paraméterek
 * */
drop table my_test_table;

create table my_test_table(
my_id integer,
comment text
);

--select * from my_test_table;
-- adat beszúrása táblába

insert into my_test_table (my_id, comment) values (2, 'valami2');
rollback;

insert into my_test_table (my_id, comment) values (4, 'valami4');


/*
 * Session - az adatbázis felé nyitott kapcsolat, ami utasítást "futtat" az adatbázisban
 * élő - idle (tétlen)
 * minden utasítás a session-ön belül történik, és csak akkor lép érvénybe
 * ha a session-ön belül végzett folyamatot valamilyen módon lezárom.
 * 
 * Tranzakció
 * 2 féle lezárása lehet: sikeres - sikertelen
 * sikeres - commit - jóváhagyom az utasítást, akkor commit
 * sikertelen - rollback - ha vissza akarom vonni, akkor rollback
 * 
 * le nem zárt tranzakció
 * blokkolhatja az adott objektum használatát: lock
 * 	- sorszintű
 *  - tábla szintű
 * 
 * a session önálló életet él, csak a lezárt tranzakció után lesz a változás
 * globálisaan elérhető az adatbázisban
 * 
 * */

