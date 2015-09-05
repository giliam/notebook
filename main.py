# coding: utf-8
from bottle import Bottle, run, view, static_file, request

app = Bottle()

@app.route('/')
@view('html/index.tpl')
def hello():
    return ({})

@app.post('/add/link')
@view('html/link.tpl')
def add_link_POST():
    """
        Adds the link to the database for post request (AJAX)
    """
    link = request.forms.get('link')
    # Adds the link in the database and get the ID
    link_id = 1
    return ({'id':link_id,'link':link})

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