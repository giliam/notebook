# coding:utf-8
import sqlite3

def init():
    db = sqlite3.connect('bottle.db')
    db.execute("CREATE TABLE notepad (nid INTEGER PRIMARY KEY, entry TEXT NOT NULL, creation INTEGER NOT NULL)")
    db.commit()

def uses_db(func):
    def wrapped(*args, **kwargs):
        db = sqlite3.connect('bottle.db')
        return func(db, *args, **kwargs)
        db.close()
    return wrapped

if __name__ == '__main__':
    init()