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
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/857251e3-c95c-4211-885a-b18ee2520932)


# TASK 3 INSERT
INSERT INTO member(name,username,password) VALUES('name','test','test');  
INSERT INTO member(name,username,password) VALUES('name1','test1','test1');  
INSERT INTO member(name,username,password) VALUES('name2','test2','test2');  
INSERT INTO member(name,username,password) VALUES('name3','test3','test3');  
INSERT INTO member(name,username,password) VALUES('name4','test4','test4');  
## select *  
SELECT * FROM member;  
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/748711c4-0486-4b84-9ba6-3628758bdce8)

## select & 排序 
SELECT * FROM member ORDER BY time asc;  
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/087bb8e6-53f6-4a4d-af62-27b4049816fe)

## 依TIME欄位
SELECT * FROM member ORDER BY time asc LIMIT 3 OFFSET 1;   
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/2553f4ff-3596-4939-acf2-9d3f849a446d)

## username == test
SELECT * FROM member WHERE username ='test';   
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/11854ccc-84b5-438c-966d-2460064983e3)

## username == test & password == test
SELECT * FROM member WHERE username ='test'and password ='test';   
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/89a16fe5-1274-4248-8025-d5dbcbba932b)

## update
UPDATE member SET name='test2' where username='test' ;  

![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/33f176c0-af84-4753-8bec-c324c93accef)


# TASK 4 COUNT
SELECT COUNT(*) FROM member;  
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/f23827db-539f-4d5c-b41e-be149bf05a0d)

## follow_count 
SELECT SUM(follower_count) FROM member;   

## 平均 
SELECT AVG(follower_count) FROM member;  

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
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/d553f057-2b89-48b0-b38a-3ce2c232cde9)

## join
SELECT * FROM member INNER JOIN message ON member.id = message.member_id;  
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/ac14e79d-c64e-455b-9262-8d3e74f9323e)

## join where
SELECT * FROM member INNER JOIN message ON member.id = message.member_id WHERE username='test';  
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/99c43308-aa30-4194-b5a0-6f2a1bd71969)  

## join where avg
SELECT AVG(like_count) FROM member INNER JOIN message ON member.id = message.member_id WHERE username='test';
![image](https://github.com/Vincent23412/Vincent23412.github.io/assets/87458133/8b65faf1-acac-45a3-9a0e-a9ba162cfadb)

