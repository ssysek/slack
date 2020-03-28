create table if not exists users
(
	user_id serial,
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
