create table User(username varchar(30) , name varchar(30),password varchar(32), 
	age int, email varchar(50), primary key(username));
create table Community(community_id varchar(30), community_name varchar(30),member_count int, 
	post_count int, primary key(community_id));
create table Post(post_id varchar(30), username varchar(30), content varchar(500), 
	rating float(6,2), community_id varchar(30), post_date date,primary key(post_id), 
	foreign key(username) references User(username), foreign key(community_id) 
	references Community(community_id));
create table Bookmark(username varchar(30),post_id varchar(30),
	primary key(username,post_id), foreign key(username) references User(username), 
	foreign key(post_id) references Post(post_id));
create table Tags(tag_id varchar(30), tag_name varchar(30), member_count int, primary key(tag_id));
create table Request(request_id varchar(30), username varchar(30), content varchar(500),
	primary key(request_id), foreign key(username) references User(username));
create table Post_tags(post_id varchar(30), tag_id varchar(30), primary key(post_id,tag_id),
	foreign key(post_id) references Post(post_id), foreign key(tag_id) references
	Tags(tag_id));
create table Request_tag(request_id varchar(30), tag_id varchar(30), primary key(request_id,tag_id),
	foreign key(request_id) references Request(request_id), foreign key(tag_id) references
	Tags(tag_id));
create table Prerequisite(post_id_1 varchar(30), post_id_2 varchar(30), primary key
	(post_id_1, post_id_2), foreign key(post_id_1) references Post(post_id), foreign key
	(post_id_2) references Post(post_id));
create table User_community(username varchar(30), community_id varchar(30), user_rating float(6,2),
	primary key(username,community_id), foreign key(username) references User(username),
	foreign key(community_id) references Community(community_id));
create table Follower(username_1 varchar(30), username_2 varchar(30), primary key
	(username_1, username_2), foreign key(username_1) references User(username),
	foreign key(username_2) references User(username));
-- username_1 is follower of username_2