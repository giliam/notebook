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

@app.route('/links')
@view('html/links.tpl')
@uses_db
def links(db):
    links = db.execute('SELECT lid, link FROM links').fetchall()
    return ({'links':links})

@app.post('/add/link')
@view('html/link.tpl')
@uses_db
def add_link_POST(db):
    """
        Adds the link to the database for post request (AJAX)
    """
    link = request.forms.get('link')
    # Adds the link in the database and get the ID
    cursor = db.execute('INSERT INTO links(link, creation) VALUES(?, ?)', (link, datetime.now()))
    db.commit()
    return ({'id':cursor.lastrowid,'link':link})

@app.put('/edit/link/<link_id:int>')
@uses_db
def edit_link(db, link_id):
    """
        Edit the link from the database
    """
    link = request.forms.get('link')
    # Edit the link in the database
    db.execute('UPDATE links SET link = ? WHERE lid = ?', (link,link_id))
    db.commit()
    return ""

@app.delete('/delete/link/<link_id:int>')
@uses_db
def delete_link(db, link_id):
    """
        Delete the link from the database
    """
    db.execute('DELETE FROM links WHERE lid = ?', (link_id,))
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