from sqlalchemy import *
engine=create_engine('sqlite:///college.db',echo=True)
meta=MetaData()
students = Table('students', meta, Column('id', Integer, primary_key=True),
Column('name', String), Column('lastname', String), )
meta.create_all(engine)
departments=Table('departments',meta, Column('dep_id', Integer), Column('dep_name', String),)
meta.create_all(engine)
marks=Table('marks', meta , Column('mark_id', Integer, primary_key=True ), Column('sub1' ,Float), Column('sub2' ,Float), Column('sub3' ,Float),Column('sub4' ,Float),Column('sub5' ,Float),)
meta.create_all(engine)
conn=engine.connect()
ins=students.insert().values(name='Nahva',lastname='C')
conn.execute(students.insert(),[{'name':'Ranjinee','lastname':'R'},{'name':'Nafeesathul','lastname':'Kamariyya'},{'name':'Nadiya','lastname':'Hafsath'},])
for i in conn.execute(students.select()):
    print(i)
conn.commit()
conn.close()
conn.execute(students.select()).fetchone()
result=conn.execute(students.select())
result.fetchall()
conn.execute(students.select().where(students.c.id>2)).fetchall()
conn.execute(students.select()).fetchmany(3)
t=text('select * from students')
conn.execute(t).fetchall()
t=text('select students.name,students.lastname from students where students.id> :x')
conn.execute(t,{'x':2}).fetchall()
st=students.alias()
conn.execute(st.select()).fetchall()
conn.execute(students.update().where(students.c.lastname=='C').values(lastname='noor'))
conn.execute(students.select()).fetchall()
conn.execute(students.delete().where(students.c.id==4))
conn.execute(students.select()).fetchall()
add=Table('address', meta, Column('id', Integer,primary_key=True), Column('st_id', Integer,ForeignKey('students.id')),Column('city', String),Column('country', String),)
meta.create_all(engine)
conn.execute(add.insert(), [
{'st_id':1, 'city':'Makkaraparamba',
'country':'India'},
{'st_id':1, 'city':'Mannarkkad',
'country':'India'},
{'st_id':3, 'city':'Hyderabad',
'country':'India'},
{'st_id':4, 'city':'Bangaluru',
'country':'India'},
{'st_id':2, 'city':'new Delhi',
'country':'India'},
])
conn.execute(add.select()).fetchall()


engine=create_engine("mysql://root:root@localhost/college",echo=True)
meta=MetaData()
students=Table('students', meta, Column('id', Integer, primary_key=True),
Column('name', VARCHAR(20)), Column('lastname', VARCHAR(20)), )
meta.create_all(engine)
conn=engine.connect()
conn.insert(students.)