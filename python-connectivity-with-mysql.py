import mysql.connector as c
con=c.connect(
    host='localhost',
    user='root',
    password='123456')
if con.is_connected () :
    print("connected successfull ")
cur=con.cursor()
cur.execute('create database if not exists school')
cur.execute('use school')
cur.execute('create table if not exists student (roll integer(7) primary key,name varchar(50),marks integer(3))')
con.commit()
while True:
    choice=int(input("1->data insert\n2->data retrieve\n3->update data\n4->data delete\n5->display all data\n6->exit\nEnter your choice:"))
    if choice==1:
        roll=int(input("enter roll number "))
        name=input("enter name ")
        marks=int(input("enter marks "))
        cur.execute("insert into student values({},'{}',{})".format(roll,name,marks))
        con.commit()
        print("row interest successfully. . .")
    elif choice==2:
        roll=int(input("enter roll number to find :"))
        cur.execute("select*from student where roll={}".format(roll))
        data=cur.fetchone()
        if cur.rowcount==0:
            print("Roll Number not found. . .")
        else:
            print(data)
    elif choice==3:
        roll=int(input("enter roll number to find :"))
        marks=int(input("enter update marks"))
        cur.execute("update student set marks={} where roll={}".format(marks,roll))
        con.commit()
        data=cur.fetchone()
        if cur.rowcount==0:
            print("Roll Number not found. . .")
        else:
            print("Data update successfully. . .")
    elif choice==4:
        roll=int(input("enter roll number to delete :"))
        cur.execute("delete from student where roll={}".format(roll))
        con.commit()
        data=cur.fetchone()
        if cur.rowcount==0:
            print("Roll Number not found. . .")
        else:
            print("data delete successfully. . .")
    elif choice==5:
        
        cur.execute("select*from student")
        data=cur.fetchall()
        if cur.rowcount==0:
            print("empty table. . .")
        else:
            for i in data:
                print(i)
    elif choice==6:
        break
    else:
        print("wrong choice")
    
