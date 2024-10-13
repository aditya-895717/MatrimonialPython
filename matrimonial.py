#Program to provide details and search for bride and groom
import mysql.connector as sql
conn = sql.connect(host='localhost', user='root', passwd='8953', database='shadi')
if conn.is_connected():
     c1 = conn.cursor()
print('_WELCOME   TO ADITYA  MARTIMONIAL  SERVICE_')
while True:
    print("1. Provide details")
    print('2. In search of bride/groom')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        print('5. Male customer details')
        print('6. Female customer details')
        choice = int(input('enter the choice:-'))
        if choice == 5 :
            asa
            
            a = input('Enter the name: ')
            b = input('Enter the address: ')
            c = input('Enter the caste: ')
            d = input('Enter the appreance: ')
            e = int(input('Enter the age: '))
            f = input('Enter the profession: ')
            g = int(input('Enter the phone_no: '))
            c1 = conn.cursor()
            sql_insert = f"INSERT INTO legends_details VALUES('{a}', '{b}', '{c}', '{d}', '{e}', '{f}', '{g}');"
            c1.execute(sql_insert)
            conn.commit()
            print('Data inserted')
            c = input('Do you want to continue (y/n)? ')
        if c.lower() == 'y':
            continue
        else:
            print('THANK  YOU  FOR  VISITING  OUR   WEBSITE' )
            print('VISIT  AGAIN')
            break
    elif choice == 6:
        h = input('Enter the name: ')
        i = input('Enter the address: ')
        j = input('Enter the caste: ')
        k = input('Enter the appreance: ')
        l = int(input('Enter the age: '))
        m = input('Enter the profession: ')
        n = int(input('Enter the phone_no: '))
        c1 = conn.cursor()
        sql_insert = f"INSERT INTO girls_details VALUES('{h}', '{i}', '{j}', '{k}', '{l}', '{m}', '{n}');"
        c1.execute(sql_insert) 
        conn.commit()
        print('Data inserted')
        c = input('Do you want to continue (y/n)? ')
        if c.lower() == 'y':
            continue
        else:
            print('THANK  YOU  FOR  VISITING  OUR   WEBSITE' )
            print('VISIT  AGAIN')
            break
        
         
