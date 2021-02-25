
from database import DatabaseManager
import pytest


db = DatabaseManager('bookmarks.db')
def test_Create_table():
       db.create_table('bookmarks_Test', {
            'id': 'integer primary key autoincrement',
            'title': 'text not null',
            'url': 'text not null',
        })
       
       table = db._execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='bookmarks_Test' ''')
       Actualcount = 0
       if table.fetchone()[0]==1 : 
	       Actualcount = 1
        
       assert Actualcount == 1

def test_add():
       data ={'title': 'Test_Add', 'url': 'AddUrl'}
       db.add('bookmarks_Test', data)
       cr = {'title':'Test_Add'}
       row = db.select('bookmarks_Test',cr).fetchone()[1]
       assert row == 'Test_Add'

def test_delete():
     data ={'title': 'Test_delete', 'url': 'DeleteUrl'}
     db.add('bookmarks_Test', data)
     cr = {'title':'Test_delete'}
     row1 = db.delete('bookmarks_Test',cr)
     row = db.select('bookmarks_Test',cr).fetchone()
     assert row == None

def test_select():
     cr = {'url':'AddUrl'}
     row = db.select('bookmarks_Test',cr).fetchone()[2]
     assert row == 'AddUrl'