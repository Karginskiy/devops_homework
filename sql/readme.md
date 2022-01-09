- Используя docker поднимите инстанс PostgreSQL (версию 12) c 2 volume, в который будут складываться данные БД и бэкапы.

Приведите получившуюся команду или docker-compose манифест.

```
./docker-compose.yml
```
- создайте пользователя test-admin-user и БД test_db
- в БД test_db создайте таблицу orders и clients (спeцификация таблиц ниже)
- предоставьте привилегии на все операции пользователю test-admin-user на таблицы БД test_db
- создайте пользователя test-simple-user
- предоставьте пользователю test-simple-user права на SELECT/INSERT/UPDATE/DELETE данных таблиц БД test_db

```
итоговый список БД после выполнения пунктов выше - https://ibb.co/PG07Wdj
описание таблиц (describe) - https://ibb.co/x8Hn3tj
SQL-запрос для выдачи списка пользователей с правами над таблицами test_db - \dp
список пользователей с правами над таблицами 
- postgres=arwdDxt/postgres
- test_simple_user=arwd/postgres
- postgres=arwdDxt/postgres
- test_simple_user=arwd/postgres
```

- Используя SQL синтаксис - наполните таблицы следующими тестовыми данными:

```
INSERT INTO orders ("Наименование", "цена") 
VALUES (
    ('Шоколад', 10), 
    ('Принтер', 3000), 
    ('Книга', 500), 
    ('Монитор', 7000), 
    ('Гитара', 4000)
);

INSERT INTO clients ("ФИО", "Страна проживания") 
VALUES (
    ('Иванов Иван Иванович', 'USA'), 
    ('Петров Петр Петрович', 'Canada'),
    ('Иоганн Себастьян Бах', 'Japan'),
    ('Ронни Джеймс Дио', 'Russia'),
    ('Ritchie Blackmore', 'Russia')
);

SELECT COUNT(*) FROM clients;
SELECT COUNT(*) FROM orders;
```

- Часть пользователей из таблицы clients решили оформить заказы из таблицы orders. Используя foreign keys свяжите записи из таблиц, согласно таблице:
```
UPDATE clients SET order_id = (SELECT id FROM orders WHERE orders.наименование = 'Книга') WHERE "ФИО" = 'Иванов Иван Иванович';
UPDATE clients SET order_id = (SELECT id FROM orders WHERE orders.наименование = 'Монитор') WHERE "ФИО" = 'Петров Петр Петрович';
UPDATE clients SET order_id = (SELECT id FROM orders WHERE orders.наименование = 'Гитара') WHERE "ФИО" = 'Иоганн Себастьян Бах';

select * from clients where order_id IS NOT NULL;

 id |         ФИО          | Страна проживания | order_id
----+----------------------+-------------------+----------
  1 | Иванов Иван Иванович | USA               |        3
  2 | Петров Петр Петрович | Canada            |        4
  3 | Иоганн Себастьян Бах | Japan             |        5

```

- Получите полную информацию по выполнению запроса выдачи всех пользователей из задачи 4 (используя директиву EXPLAIN).

```
                         QUERY PLAN
------------------------------------------------------------
 Seq Scan on clients  (cost=0.00..10.70 rows=70 width=1040)
   Filter: (order_id IS NOT NULL)
(2 rows)

Означает, что запрос производит последовательных проход по таблице и фильтрацию по условию в Filter: 

```

- Создайте бэкап БД test_db и поместите его в volume, предназначенный для бэкапов (см. Задачу 1).
- Остановите контейнер с PostgreSQL (но не удаляйте volumes).
- Поднимите новый пустой контейнер с PostgreSQL.
- Восстановите БД test_db в новом контейнере.

```
pg_dump -U postgres devops_homework > /var/lib/postgresql/dumps/devops_homework.tar
docker run --rm --user postgres -v ./dumps:/dumps ubuntu bash -c "cd /dumps && tar xvf /dumps/devops_homework.tar --strip 1" 
