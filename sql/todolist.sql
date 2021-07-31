drop table if exists todolist;
--drop table if exists task_status;

--CREATE TABLE task_status(
    --id serial primary key,
   -- name text,
    --terminal boolean
   -- );

--insert into task_status (name,terminal) values ('In progress',FALSE);
--insert into task_status (name,terminal) values ('TODO',FALSE);
--insert into task_status (name,terminal) values ('Complete',FALSE);


--CREATE TABLE todolist(
--    id SERIAL PRIMARY KEY NOT NULL,
--    task TEXT UNIQUE NOT NULL,
--    status serial references task_status(id)
--    );


--select t.id, t.task, s.name from todolist t, task_status s where s.id=t.status;

CREATE TABLE todolist(
    id SERIAL PRIMARY KEY NOT NULL,
    task TEXT UNIQUE NOT NULL,
    description TEXT UNIQUE NOT NULL,
    status TEXT DEFAULT 'TODO' NOT NULL
    );
