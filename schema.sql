drop table if exists logins;
create table logins (
  id integer primary key autoincrement,
  username text not null,
  password text not null
);

drop table if exists accounts;
create table accounts (
	accountname text primary key,
	type text not null,
	balance integer not null
);
