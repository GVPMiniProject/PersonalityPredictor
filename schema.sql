drop table if exists userDetails;
create table userDetails (
	userId integer primary key autoincrement,
    userName text not null,
	password text not null,
	userType text not null
);

drop table if exists queDetails;
create table queDetails (
	queId integer primary key autoincrement,
    queDesc text not null,
	opt1 text not null,
	opt2 text not null,
	opt3 text not null,
	opt4 text not null,
	answer text not null
);

drop table if exists testResult;
create table testResult (
	testId integer primary key autoincrement,
    userId integer not null,
	t_date date not null,
	t_time time not null,
	score integer not null
);

