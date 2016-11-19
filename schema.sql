drop table if exists logins;
create table logins (
  id integer primary key autoincrement,
  username text not null unique,
  password text not null
);

drop table if exists accounts;
create table accounts (
	id integer primary key autoincrement,
	username text not null,
	accountname text not null,
	type text not null,
	balance real not null
);

drop table if exists transactions;
create table transactions (
	id integer primary key autoincrement,
	timestamp datetime default current_timestamp,
	username_1 text,
	account_1 text,
	username_2 text,
	account_2 text,
	amount real,
	type text
);