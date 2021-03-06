
from database import DatabaseManager
from datetime import datetime
import sqlite3
import os
import pytest


@pytest.fixture
def db() -> DatabaseManager:
    """
    What is a fixture? https://docs.pytest.org/en/stable/fixture.html#what-fixtures-are
    """
    filename = "test_bookmarks.db"
    dbm = DatabaseManager(filename)
    yield dbm
    dbm.__del__()           # explicitly release the database manager
    os.remove(filename)


def test_Create_table(db):
       db.create_table("bookmarks_Test",
        {
            "id": "integer primary key autoincrement",
            "title": "text not null",
            "url": "text not null",
            "notes": "text",
            "date_added": "text not null",
        }, )
    #assert
       conn = db.connection
       cursor = conn.cursor()

       table = cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='bookmarks_Test' ''')
     
       assert table.fetchone()[0] == 1
    #cleanup
       db.drop_table("bookmarks_Test")


def test_add(db):
      db.create_table("bookmarks_Test",
        {
            "id": "integer primary key autoincrement",
            "title": "text not null",
            "url": "text not null",
            "notes": "text",
            "date_added": "text not null",
        }, )

      data ={'title': 'Test_Add', 'url': 'AddUrl', "date_added": datetime.utcnow().isoformat() }
      db.add('bookmarks_Test', data)
       
      conn = db.connection
      cursor = conn.cursor()
      cursor.execute(''' SELECT * FROM bookmarks_Test WHERE title='Test_Add' ''') 
      assert cursor.fetchone()[0] ==1


def test_select(db):
      db.create_table("bookmarks_Test",
        {
            "id": "integer primary key autoincrement",
            "title": "text not null",
            "url": "text not null",
            "notes": "text",
            "date_added": "text not null",
        }, )

      data ={'title': 'Test_Add', 'url': 'AddUrl', "date_added": datetime.utcnow().isoformat() }
      db.add('bookmarks_Test', data)
      cr = {'url':'AddUrl'}

      row = db.select('bookmarks_Test',cr).fetchone()[2]
      assert row == 'AddUrl'

def test_delete(db):
     db.create_table("bookmarks_Test",
        {
            "id": "integer primary key autoincrement",
            "title": "text not null",
            "url": "text not null",
            "notes": "text",
            "date_added": "text not null",
        }, )

     data ={'title': 'Test_Add', 'url': 'DeleteUrl', "date_added": datetime.utcnow().isoformat() }
     db.add('bookmarks_Test', data)
     cr = {'title':'Test_Add'}
     db.delete('bookmarks_Test',cr)

     conn = db.connection
     cursor = conn.cursor()
     cursor.execute(''' SELECT * FROM bookmarks_Test WHERE title='Test_Add' ''') 
     
     assert cursor.fetchone() == None

