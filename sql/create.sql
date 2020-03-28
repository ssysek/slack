create table if not exists users
(
	user_id integer not null primary key,
	user_name varchar(50),
	user_surname varchar(50)
);


create table if not exists posts
(
    post_id integer not null primary key,
    owner_id integer not null
        constraint user_id,
    post_content varchar(600)
);
