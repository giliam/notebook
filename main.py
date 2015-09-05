# coding: utf-8
from bottle import Bottle, run, view, static_file

app = Bottle()
 
@app.route('/')
@view('html/index.tpl')
def hello():
    return ({})

@app.route('/add/link')
def add_link():
    """
        Adds the link to the database
    """
    return (context)

@app.route('/static/<filename:path>')
def server_static(filename):
    """
        Sert les fichiers statiques tel que .js, .css, .jpeg, etc...
    """
    return static_file(filename, root='.')

run(app, host='localhost', port=8080)