
create table if not exists users
(
	user_id serial, --serial = not null unique
	user_name varchar(50),
	user_surname varchar(50),
	password varchar(50),
	login varchar(50) unique,
	email varchar(60),
	constraint user_id_pk primary key (user_id)
);

create table if not exists posts
(
    post_id serial,
    owner_id integer not null,
    chat_id integer not null,
    post_content varchar(600),
    constraint post_id_pk primary key (post_id),
    constraint post_fk foreign key (owner_id) references users(user_id),
    constraint post_chat_fk foreign key (chat_id) references chats(chat_id)
);

create table if not exists forum_names
(
    forum_id serial,
    forum_name varchar(100),
    image integer,
    constraint forum_id_pk primary key (forum_id)
);

create table if not exists permissions
(
    forum_id integer not null,
    permitted_user integer not null,
    constraint forum_id_pk foreign key (forum_id) references forum_names(forum_id),
    constraint forum_fk foreign key (permitted_user) references users(user_id)
);

create table if not exists chats
(
    chat_id serial,
    chat_name varchar(100),
    upper_forum_id integer,
    image integer,
    constraint chat_id_pk primary key (chat_id),
    constraint upper_forum_id_fk foreign key (upper_forum_id) references forum_names(forum_id)
);

create table if not exists chat_permissions
(
    chat_id integer not null,
    permitted_user integer not null,
    constraint chat_id_pk foreign key (chat_id) references chats(chat_id),
    constraint chat_fk foreign key (permitted_user) references users(user_id)
);

create table if not exists notes
(
    note_id serial,
    title varchar(50),
    notes_content varchar(500),
    owner_id integer not null,
    constraint notes_fk foreign key (owner_id) references users(user_id)
);

create table if not exists mails
(
    mail_id serial,
    fname varchar(60),
    lname varchar(60),
    email varchar(60),
    subject varchar(60),
    message varchar(600)
);


--insert into users values (1, 'Jan', Nowak', 'janek', 'Nowaczek123');
--insert into posts values (1, 1, 1, 'Lorem ipsum');
--user_id, oraz post_id musza byc unikalne dla calej tabeli. Ponadto bedzie blad, jezeli podamy
--owner_id usera, ktore user_id nie wystepuje w tabeli users.
