create table User(username varchar(30) , name varchar(30),password varchar(32), 
	age int, email varchar(50), primary key(username));
create table Community(community_id varchar(30), community_name varchar(30),member_count int, 
	post_count int, primary key(community_id));
create table Post(post_id varchar(30), username varchar(30), content varchar(500), 
	rating float(6,2), community_id varchar(30), post_time TIMESTAMP default CURRENT_TIMESTAMP,primary key(post_id), 
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
-- post_id_1 is prerequisite of post_id_2

INSERT INTO `User` (`username`, `name`, `password`, `age`, `email`) VALUES ('piyushrathipr', 'piyush', 'areyar', '19', 'piy@gmail.com');
INSERT INTO `User` (`username`, `name`, `password`, `age`, `email`) VALUES ('fsociety00', 'shubham', 'say_hi', '20', 'fsoc@gmail.com');
INSERT INTO `web`.`User` (`username`, `name`, `password`, `age`, `email`) VALUES ('sauravray2587', 'saurav', 'temper', '20', 'sau@gmail.com');
INSERT INTO `Community` (`community_id`, `community_name`, `member_count`, `post_count`) VALUES ('0', 'codeforces', '1', '0');
INSERT INTO `Post` (`post_id`, `username`, `content`, `rating`, `community_id`) VALUES ('0', 'fsociety00', 'segment tree', '2100', '0');
INSERT INTO `Post` (`post_id`, `username`, `content`, `rating`, `community_id`) VALUES ('1', 'fsociety00', 'dsu', '2100', '0');
INSERT INTO `Post` (`post_id`, `username`, `content`, `rating`, `community_id`) VALUES ('2', 'piyushrathipr', 'storing segment tree history', '1900', '0');
INSERT INTO `Follower` (`username_1`, `username_2`) VALUES ('piyushrathipr', 'fsociety00');

INSERT INTO `Tags` (`tag_id`) VALUES ('dp');
INSERT INTO `Tags` (`tag_id`) VALUES ('greedy');
INSERT INTO `Post_tags` (`post_id`, `tag_id`) VALUES ('1', 'greedy');
INSERT INTO `Post_tags` (`post_id`, `tag_id`) VALUES ('2', 'greedy');

INSERT INTO `User_community` (`username`, `community_id`, `user_rating`) VALUES ('fsociety00', '0', '2100');
INSERT INTO `User_community` (`username`, `community_id`, `user_rating`) VALUES ('piyushrathipr', '0', '1900');

UPDATE `web`.`User_community` SET `user_rating`='1900' WHERE `username`='piyushrathipr' and`community_id`='0';
INSERT INTO `web`.`User_community` (`username`, `community_id`, `user_rating`) VALUES ('sauravray2587', '0', '1910');










USE `web`;

DELIMITER $$

DROP TRIGGER IF EXISTS web.Post_AFTER_INSERT$$
USE `web`$$
CREATE DEFINER = CURRENT_USER TRIGGER `web`.`Post_AFTER_INSERT` AFTER INSERT ON `Post` FOR EACH ROW
BEGIN
UPDATE `web`.`Community` SET `Community`.member_count = `Community`.member_count + 1 WHERE `Community`.community_id = NEW.community_id;
END$$
DELIMITER ;




USE `web`;

DELIMITER $$

DROP TRIGGER IF EXISTS web.User_community_AFTER_INSERT$$
USE `web`$$
CREATE DEFINER = CURRENT_USER TRIGGER `web`.`User_community_AFTER_INSERT` AFTER INSERT ON `User_community` FOR EACH ROW
BEGIN
UPDATE `web`.`Community` SET `Community`.member_count = `Community`.member_count + 1 WHERE `Community`.community_id = NEW.community_id;
END$$
DELIMITER ;