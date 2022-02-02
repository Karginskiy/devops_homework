- Используя docker поднимите инстанс PostgreSQL (версию 13). Данные БД сохраните в volume.
- Подключитесь к БД PostgreSQL используя psql.
- Воспользуйтесь командой \? для вывода подсказки по имеющимся в psql управляющим командам.
- Найдите и приведите управляющие команды для:
    - вывода списка БД
    - подключения к БД
    - вывода списка таблиц
    - вывода описания содержимого таблиц
    - выхода из psql

```
Вывод списка бд - \l[+]   [PATTERN]
Подключение к БД - \c[onnect] {[DBNAME|- USER|- HOST|- PORT|-] | conninfo}
Вывод списка таблиц -   \d
Вывод описания списка таблиц - \dt
Выход - \q
```

- Используя psql создайте БД test_database.

- Изучите бэкап БД.

- Восстановите бэкап БД в test_database.

- Перейдите в управляющую консоль psql внутри контейнера.

- Подключитесь к восстановленной БД и проведите операцию ANALYZE для сбора статистики по таблице.

- Используя таблицу pg_stats, найдите столбец таблицы orders с наибольшим средним значением размера элементов в байтах.

- Приведите в ответе команду, которую вы использовали для вычисления и полученный результат.

```
 select attname, avg_width from pg_stats where tablename = 'orders' ORDER BY avg_width DESC LIMIT 1;
 ```

- Архитектор и администратор БД выяснили, что ваша таблица orders разрослась до невиданных размеров и поиск по ней занимает долгое время. Вам, как успешному выпускнику курсов DevOps в нетологии предложили провести разбиение таблицы на 2 (шардировать на orders_1 - price>499 и orders_2 - price<=499).

- Предложите SQL-транзакцию для проведения данной операции.

```
BEGIN;

create table orders_1 ( CHECK (price > 499)) INHERITS (orders);
create table orders_1 ( CHECK (price > 499)) INHERITS (orders);

WITH deleted_orders_gt_499 AS ( DELETE FROM ONLY orders WHERE price > 499 RETURNING *) INSERT INTO orders_1 SELECT * FROM deleted_orders_gt_499;

WITH deleted_orders_le_499 AS ( DELETE FROM ONLY orders WHERE price <= 499 RETURNING *) INSERT INTO orders_2 SELECT * FROM deleted_orders_le_499;

COMMIT;
```

- Можно ли было изначально исключить "ручное" разбиение при проектировании таблицы orders?

```
Можно было изначально создать правила партицирования для orders используя PARTINION OF
```

- Используя утилиту pg_dump создайте бекап БД test_database.

- Как бы вы доработали бэкап-файл, чтобы добавить уникальность значения столбца title для таблиц test_database?

```

Можно в этом месте дампа:

--
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    id integer NOT NULL,
    title character varying(80) NOT NULL,
    price integer DEFAULT 0
);

добавить в определение колонки title добавить UNIQUE таким образом:

title character varying(80) NOT NULL UNIQUE,
```


