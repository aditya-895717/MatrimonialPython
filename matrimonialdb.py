#Program to create required tables in database

	import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', password='P@ssword',      database='shadi')
c1 = conn.cursor()
c1.execute('CREATE TABLE legends_details(name varchar(100), address varchar(100), caste varchar(100), appearance varchar(100), age int(4), profession varchar(65), phone_no  bigint(15));')
c1.execute('CREATE TABLE girls_details(name varchar(100), address varchar(100), caste varchar(50), appearance varchar(100), age int(4),
profession varchar(65), phone_no bigint(15));')
c1.execute('CREATE TABLE user_id(user_name varchar(100), password varchar(55));')
conn.commit()
