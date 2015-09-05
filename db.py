# coding:utf-8
import sqlite3

db = sqlite3.connect('bottle.db')
db.execute("CREATE TABLE links (id INTEGER PRIMARY KEY, link TEXT NOT NULL, creation INTEGER NOT NULL)")
db.commit()