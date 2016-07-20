# -*- coding: utf-8 -*-

import sqlite3
import os
import sys


class _QueryIn:
    def __init__(self, query, database_file):
        self.database_file = database_file
        self.query = query
        self.data = []
        
    def push(self, *args):
        self.data.append(args)
        return self
    
    def commit(self):
        
        con = sqlite3.connect(self.database_file)
        cur = con.cursor()
        
        if len(self.data) > 0:
            cur.executemany(self.query, self.data)
        else:
            cur.execute(self.query)
            
        con.commit()
        con.close()


class _QueryOut:
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
    
    def __init__(self, query, database_file):
        self.database_file = database_file
        self.query = query
        
    def commit(self):
        con = sqlite3.connect( self.database_file )
        con.row_factory = self.dict_factory
        cur = con.cursor()
        cur.execute(self.query)
        res = cur.fetchall()
        con.commit()
        con.close()
        
        if len(res) != 0:
            return res
        else:
            return None




class DB:
    """
    SQLite3 database wrapper. 
    Manuel Arturo Izquierdo <aizquier@gmail.com> 2015
    
    Usage:
    
    # * initilaize DB object
    mydb = DB('database_file.sqlite')
    
    # * Query out data (results in dict data):
    data = mydb.QueryOut('select * from table').commit()
    
    # * Query in data
    query = mydb.QueryIn(
      'insert into table (col1, col2, ... ,coln) values (?, ?, ... , ?)')
      
    # * push as many fields as required...
    query.push((val1, val2, ..., valn))
    query.push((val1, val2, ..., valn))
    ...
    
    # * finally commit all the data:
    query.commit()
    
    """
    
    def __init__(self, database_file, mode='r'):
        self.database_file = database_file
        
        if mode == 'w':
            if os.path.exists(self.database_file):
                os.remove(self.database_file)
                #self.database_file += '.new'
        
    def QueryOut(self, query):
        return _QueryOut(query, self.database_file)
        
            
    def QueryIn(self, query):
        return _QueryIn(query, self.database_file)
            
            
            
            
            
            
            
        
