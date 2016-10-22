drop table if exists logins;
create table logins (
  id integer primary key autoincrement,
  username text not null,
  password text not null
);

drop table if exists accounts;
create table accounts (
	id integer primary key autoincrement,
	accountname text not null,
	type text not null,
	amount integer not null
);
