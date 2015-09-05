# coding: utf-8
from bottle import Bottle, run, view, static_file, request, install
from bottle_sqlite import SQLitePlugin
from datetime import datetime

app = Bottle()
install(SQLitePlugin(dbfile='/bottle.db'))

@app.route('/')
@view('html/index.tpl')
def index():
    return ({})

@app.route('/links')
@view('html/links.tpl')
def links():
    return ({})

@app.post('/add/link')
@view('html/link.tpl')
def add_link_POST(db):
    """
        Adds the link to the database for post request (AJAX)
    """
    link = request.forms.get('link')
    # Adds the link in the database and get the ID
    row = db.execute('INSERT INTO links(link, creation) VALUES(?, ?)', (link, datetime.now()))
    print row
    row = db.execute('SELECT * from links where link=?', item).fetchone()
    return ({'id':row['id'],'link':link})

@app.put('/edit/link/<link_id:int>')
def edit_link(link_id):
    """
        Edit the link from the database
    """
    link = request.forms.get('link')
    # Edit the link in the database
    print link_id
    return ""

@app.delete('/delete/link/<link_id:int>')
def delete_link(link_id):
    """
        Delete the link from the database
    """
    print link_id
    return ""

@app.route('/static/<filename:path>')
def server_static(filename):
    """
        Sert les fichiers statiques tel que .js, .css, .jpeg, etc...
    """
    return static_file(filename, root='.')

run(app, host='localhost', port=8080)