import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  
  
  database = "CRUD"
)

print(mydb)
print("connected successfully")

# mydb.cursor()
cursorObject = mydb.cursor()

# creating database
# create_databases=cursorObject.execute("CREATE DATABASE student;")
# print(show_databases)

# modified_student_table=cursorObject.execute('''ALTER TABLE student MODIFY COLUMN student_id INT auto_increment''')

created=cursorObject.excute('SHOW TABLES;')
myresult=cursorObject.fetchall()
for x in myresult:
  print(x)



#inserting data into table
# inserting_student_table=cursorObject.execute('''INSERT INTO  student(student_id,name,city,roll) 
# VALUES(2,"Shahid Gujar","Nepalgun",100);''')

# dynamically_inserting_student

"""sql='''INSERT INTO STUDENT(name,city,roll)
    VALUES(%s,%s,%s)

    '''

val=("Raghav Gupta","Ludhiana",45)
cursorObject.execute(sql,val)"""

#inserting many values at once
'''val = [(5,"Nikhil", "CSE", "98"),
       (6,"Nisha", "CSE", "99"),
       (7,"Rohan", "MAE", "43"),
       (8,"Amit", "ECE", "24"),
       (9,"Anil", "MAE", "45"),
       (10,"Megha", "ECE", "55"),
       (11,"Sita", "CSE", "95")]
   
cursorObject.executemany(sql, val)'''

#Updating Data
"""sql='''
UPDATE  student  
    set roll=46
    where roll=45;
    

    ''' 
  

cursorObject.execute(sql)"""

#Deleting Data
"""sql='''
DELETE FROM  student  
    
    where roll=46;
    

    '''

cursorObject.execute(sql)"""

#Retrieving Data from Databbase
"""sql='''
  SELECT * FROM  student ; 
  '''

cursorObject.execute(sql)
query=cursorObject.fetchall()
for result in query:
  print(result)
  """
#until we donot commit no data will be saved in DB
mydb.commit()

# Disconnecting from the server
mydb.close()
