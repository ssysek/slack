create table if not exists users
(
	user_id serial, --serial = not null unique
	user_name varchar(50),
	user_surname varchar(50),
	constraint user_id_pk primary key (user_id)
);


create table if not exists posts
(
    post_id serial,
    owner_id integer not null,
    post_content varchar(600),
    constraint post_id_pk primary key (post_id),
    constraint post_fk foreign key (owner_id) references users(user_id)
);


--insert into users (user_id, user_name, user_surname) values (1, 'Jan', Nowak');
--insert into posts (post_id, owner_id, content) values (1, 1, 'Lorem ipsum');
--user_id, oraz post_id musza byc unikalne dla calej tabeli. Ponadto bedzie blad, jezeli podamy
--owner_id usera, ktore user_id nie wystepuje w tabeli users.
