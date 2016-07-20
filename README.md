# Simple SQLite3 database wrapper. 

Manuel Izquierdo <aizquier@gmail.com> 2015

A very simple python wrapper for working with sqlite3 databases that I wrote for some of my projects. Not absolutely 
perfect, but it does the job. 

## Usage:

Initialize DB object

    from pssw.db import DB
    mydb = DB('database_file.sqlite')

Query out data (results in dict data):

    data = mydb.QueryOut('select * from table').commit()

Query in data

    query = mydb.QueryIn(
      'insert into table (col1, col2, ... ,coln) values (?, ?, ... , ?)')
  
push as many fields as required...

    query.push((val1, val2, ..., valn))
    query.push((val1, val2, ..., valn))
    ...

finally commit all the data:

    query.commit()
