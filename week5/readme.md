# TASK 2 CREATE DATABASE TABLE
SHOW databases;  
CREATE database website;  
USE website;  
SHOW tables;  
SELECT * FROM member;  
## TABLE
CREATE table member(  
	id bigint primary KEY auto_increment,  
    name VARCHAR(255) NOT NULL,  
    username VARCHAR(255) NOT NULL,  
    password VARCHAR(255) NOT NULL,  
    follower_count INT unsigned NOT NULL default 0,  
    time datetime NOT NULL DEFAULT NOW()  
);   
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/ceced2ba-82af-45e0-9ff7-915d55415cd3)



# TASK 3 INSERT
INSERT INTO member(name,username,password) VALUES('name','test','test');  
INSERT INTO member(name,username,password) VALUES('name1','test1','test1');  
INSERT INTO member(name,username,password) VALUES('name2','test2','test2');  
INSERT INTO member(name,username,password) VALUES('name3','test3','test3');  
INSERT INTO member(name,username,password) VALUES('name4','test4','test4');  
## select *  
SELECT * FROM member;  
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/f1f46683-8e6e-4172-a596-6a7d27fcf29d)


## select & 排序 
SELECT * FROM member ORDER BY time asc;  
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/2a2ffa6f-4aa5-4bd9-96c0-7ff25f192400)


## 依TIME欄位
SELECT * FROM member ORDER BY time asc LIMIT 3 OFFSET 1;   
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/b67aaee5-4422-4995-acce-c556e62b8db6)


## username == test
SELECT * FROM member WHERE username ='test';   
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/2f65b716-f12f-44df-a1a6-8cf53cae0721)


## username == test & password == test
SELECT * FROM member WHERE username ='test'and password ='test';   
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/f89504a4-ea50-4a0f-a079-10825875331f)


## update
UPDATE member SET name='test2' where username='test' ;  

![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/2fce5fb9-e375-48f4-a16a-4a58a39bf3d8)


# TASK 4 COUNT
SELECT COUNT(*) FROM member;  
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/01dea9e7-8238-4d00-8789-80d30ae5d261)


## follow_count 
SELECT SUM(follower_count) FROM member;   

## 平均 
SELECT AVG(follower_count) FROM member;  
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/1ce108a3-e79c-45ed-a5cf-8daf36227afb)

# TASK 5 FOREIGN KEY JOIN
CREATE TABLE message(  
	id BIGINT PRIMARY KEY auto_increment,  
    member_id BIGINT NOT NULL,  
    content VARCHAR(255) NOT NULL,  
    like_count INT UNSIGNED NOT NULL DEFAULT 0,  
    TIME DATETIME NOT NULL DEFAULT NOW()  
);  
INSERT INTO message(member_id,content) VALUES(1,'hello');  
INSERT INTO message(member_id,content) VALUES(3,'hi');  
INSERT INTO message(member_id,content) VALUES(5,'welcome');  
INSERT INTO message(member_id,content) VALUES(1,'你好');  
ALTER TABLE message ADD FOREIGN KEY(member_id) REFERENCES member(id);  
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/9ad7d97e-d33f-4421-83e5-2bb2d0239de8)


## join
SELECT * FROM member INNER JOIN message ON member.id = message.member_id;  
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/1ef6ba32-91d9-42bb-8e50-ea003b3cfdd4)


## join where
SELECT * FROM member INNER JOIN message ON member.id = message.member_id WHERE username='test';  
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/d99f3b7f-d2f5-4be1-8f92-8cb4e3ccdc3f)


## join where avg
SELECT AVG(like_count) FROM member INNER JOIN message ON member.id = message.member_id WHERE username='test';
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/709c6f75-b1ce-48e0-8a82-10c4fdfab6ba)


