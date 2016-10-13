drop table if exists logins;
create table logins (
  id integer primary key autoincrement,
  username text not null,
  password text not null
);