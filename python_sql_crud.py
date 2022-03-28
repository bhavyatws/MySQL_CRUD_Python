#MySQL crud with Python
#library =>pip install pip install mysql-connector-python

import mysql.connector

class Python_SQL_Crud():
    #Initially Constructor
    def __init__(self,host,user,password,database):
        # self.host=host
       
        self.mydb = mysql.connector.connect(
            host=host,user=user,password=password,database=database
        )
        print(self.mydb)
        self.cursorObject = self.mydb.cursor()
        print("******connected successfully*****")
    
    #show tables
    def show_tables(self):
        created=self.cursorObject.execute('SHOW TABLES;')
        myresult=self.cursorObject.fetchall()
        for x in myresult:
            print(x)

    #Insert Single Data 
    def inset_single_data(self,name,city,roll):
        sql='''INSERT INTO STUDENT(name,city,roll)
            VALUES(%s,%s,%s)'''
        self.name=name
        self.city=city
        self.roll=roll
        val=(name,city,roll)
        inserted=self.cursorObject.execute(sql,val)
        if inserted:
            print("******Data Inserted******* ")
        self.mydb.commit()
        self.mydb.close()  
    
    #Insert Multiple Data At once 
    def inset_many_data(self,many_data):
        sql='''INSERT INTO STUDENT(name,city,roll)
            VALUES(%s,%s,%s)'''
        self.many_data=many_data
        print(many_data)
        val=(many_data)
        inserted=self.cursorObject.executemany(sql,val)
        if inserted:
            print("******Data Inserted******* ")
        self.mydb.commit()
        self.mydb.close()
    
    #Updating Data
    def update_data(self,data_to_modified,student_id):
        #Updating Data
        sql='''UPDATE  student  
            set roll= %s
            where student_id= %s ;
            ''' 
        self.data_to_modified=data_to_modified
        self.student_id=student_id
        val=(data_to_modified,student_id)
        self.cursorObject.execute(sql,val)
        self.mydb.commit()
        # print(self.cursorObject.rowcount, "record(s) affected")
        self.mydb.close()

    def delete_data(self,student_id):
        #Deleting Data
        sql='''
            DELETE FROM  student  
            where student_id = %s ;

            '''
        self.student_id=student_id
        val=(id)
        self.cursorObject.execute(sql,val)
        self.mydb.commit()
        self.mydb.close()
    
    #Retrieving Data from Databbase
    def show_data(self):
        sql='''
            SELECT * FROM  student ; 
            '''
        self.cursorObject.execute(sql)
        query=self.cursorObject.fetchall()
        for result in query:
            print(result)
        self.mydb.close()
  
        

#Driver Program

crud=Python_SQL_Crud("localhost","root","","CRUD")
# crud.show_tables()
# crud.inset_single_data("Pratyush","Jhapa",189)
many_data=[
    ("Nikhil", "CE", 123),
    ("Nisha", "EEE", 124),
    ("Rohan", "BBA", 125),
    
]
# crud.inset_many_data(many_data)
# crud.update_data(101,1)
crud.show_data()

