# coding: utf-8
from bottle import Bottle, run, view, static_file, request, install
import sqlite3
from datetime import datetime
from db import uses_db

app = Bottle()

@app.route('/')
@view('html/index.tpl')
def index():
    return ({})

@app.route('/notepad')
@view('html/notepad.tpl')
@uses_db
def notepad(db):
    notepad = db.execute('SELECT nid, entry, status FROM notepad').fetchall()
    return ({'notepad':notepad})

@app.post('/notepad/add/entry')
@view('html/entry.tpl')
@uses_db
def add_entry_POST(db):
    """
        Adds the entry to the database for post request (AJAX)
    """
    entry = request.forms.get('entry')
    # Adds the entry in the database and get the ID
    cursor = db.execute('INSERT INTO notepad(entry, creation) VALUES(?, ?)', (entry, datetime.now()))
    db.commit()
    return ({'id':cursor.lastrowid,'entry':entry})

@app.put('/notepad/edit/entry/<entry_id:int>')
@uses_db
def edit_entry(db, entry_id):
    """
        Edit the entry from the database
    """
    entry = request.forms.get('entry')
    # Edit the entry in the database
    db.execute('UPDATE notepad SET entry = ? WHERE nid = ?', (entry,entry_id))
    db.commit()
    return ""

@app.put('/notepad/close/entry/<entry_id:int>')
@uses_db
def close_entry(db, entry_id):
    """
        Close the entry
    """
    # Close the entry in the database
    db.execute('UPDATE notepad SET status = 1 WHERE nid = ?', (entry_id,))
    db.commit()
    return ""

@app.put('/notepad/open/entry/<entry_id:int>')
@uses_db
def open_entry(db, entry_id):
    """
        Open the entry
    """
    # Open the entry in the database
    db.execute('UPDATE notepad SET status = 0 WHERE nid = ?', (entry_id,))
    db.commit()
    return ""

@app.delete('/notepad/delete/entry/<entry_id:int>')
@uses_db
def delete_entry(db, entry_id):
    """
        Delete the entry from the database
    """
    db.execute('DELETE FROM notepad WHERE nid = ?', (entry_id,))
    db.commit()
    return ""

@app.route('/static/<filename:path>')
def server_static(filename):
    """
        Sert les fichiers statiques tel que .js, .css, .jpeg, etc...
    """
    return static_file(filename, root='.')

if __name__ == '__main__':
    run(app, host='localhost', port=8080)