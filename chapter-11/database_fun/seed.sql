USE database_fun;
TRUNCATE TABLE authors;

insert into authors (first_name, last_name, email)
values ('Bruce', 'Van Horn', 'bruce@test.com');

insert into authors (first_name, last_name, email)
values ('Kinnari', 'Chohan', 'kinnari@test.com');

insert into authors (first_name, last_name, email)
values ('Prajakta', 'Naik', 'prajakta@test.com');

insert into authors (first_name, last_name, email)
values ('Jubit', 'Pincy', 'jubit@test.com');

SELECT *
FROM authors;