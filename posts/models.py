from django.db import models
from django.contrib.auth.models import User


  # {
  #   'title':'First post',
  #   'content':'First post content',
  #   'author':'Mahesh',
  #   'date':'30/04/2020'
  # } 
class Post(models.Model):
    title = models.CharField(max_length=200) # limited size string
    content = models.TextField() # string , but not limit
    create_date = models.DateTimeField(auto_now_add=True) # auto_now_add -> makes it immutable
    modified_date = models.DateTimeField(auto_now=True) # auto_now -> makes it mutable
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content[:25]}....'



# DBMS - Database management system - to provide a way to organise and store data
# Eg: Oracle, Mysql, sqlite..etc
# database we are using is sqlite3-RDBMS(Relational DBMS)
# RDMBS -> Tables -> columns and rows -> 
# eg:table - student register, columns -> Rollno,Name, rows-> records of each student

# To create tables in sqlite DB we need to use SQL language
# to create student register table query needed to be executed
# >>> CREATE TABLE student_register (rollno Integer, name varchar);


# ORM - Object Relational Mapping
# DBMS <-> ORM <-> python
