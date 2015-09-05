# coding: utf-8
from bottle import Bottle, run, view, static_file, request

app = Bottle()

@app.route('/')
@view('html/index.tpl')
def hello():
    return ({})

@app.post('/add/link', method="POST")
@view('html/link.tpl')
def add_link_POST():
    """
        Adds the link to the database for post request (AJAX)
    """
    link = request.forms.get('link')
    link_id = 1
    return ({'id':link_id,'link':link})

@app.get('/add/link', method="GET")
def add_link_GET():
    """
        Adds the link to the database for get request
    """
    return hello()

@app.route('/edit/link/<id:int>')
def edit_link():
    """
        Edit the link from the database
    """
    return hello()

@app.route('/delete/link/<id:int>')
def delete_link():
    """
        Delete the link from the database
    """
    return hello()

@app.route('/static/<filename:path>')
def server_static(filename):
    """
        Sert les fichiers statiques tel que .js, .css, .jpeg, etc...
    """
    return static_file(filename, root='.')

run(app, host='localhost', port=8080)