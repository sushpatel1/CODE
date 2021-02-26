import commands as commands
import pytest


commands.CreateBookmarksTableCommand().execute()

def test_Add_Bookmark_Commands():    
    data ={'title': 'testbookmark',
            'url': 'testbookmark.com',
            'notes': 'this is for test'}

    add = commands.AddBookmarkCommand().execute(data)
    assert add =='Bookmark added!'

def test_List_bookmark_Commands():
  Blist = commands.ListBookmarksCommand().execute()[0]
  assert Blist[1] == 'testbookmark'

def test_Delete_Bookmark_Commands():
    delete = commands.DeleteBookmarkCommand().execute('1')
    assert delete == 'Bookmark deleted!'
