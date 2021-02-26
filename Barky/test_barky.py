import pytest
import barky as option

options= {'A':'Add a bookmark',
          'B':'List bookmarks by date',
          'T':'List bookmarks by title',
          'D': 'Delete a bookmark',
           'Q':'Quit'}
def test_get_add_bookmark_():   
   test =  option.option_choice_is_valid('A',options)
   assert test == True

def test_get_add_bookmark1_():
   test =  option.option_choice_is_valid('S',options)
   assert test == False

def test_get_list_date_bookmark_():
   test =  option.option_choice_is_valid('B',options)
   assert test == True

def test_get_list_date_bookmark1_():
   test =  option.option_choice_is_valid('AB',options)
   assert test == False

def test_get_list_title_bookmark_():
   test =  option.option_choice_is_valid('T',options)
   assert test == True

def test_get_list_title_bookmark1_():
   test =  option.option_choice_is_valid('k',options)
   assert test == False

def test_get_delete_bookmark_():
   test =  option.option_choice_is_valid('D',options)
   assert test == True

def test_get_delete_bookmark1_():
   test =  option.option_choice_is_valid('k',options)
   assert test == False

def test_get_quit_bookmark_():
   test =  option.option_choice_is_valid('Q',options)
   assert test == True

def test_get_quit_bookmark1_():
   test =  option.option_choice_is_valid('n',options)
   assert test == False