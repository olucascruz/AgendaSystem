import sqlite3
import pathlib
import urllib.parse
from .create_db import create_db
from flask import g


def get_db():
    PATH_DB =  'agenda_db.db'

    def _path_to_uri(path):
        path = pathlib.Path(path)
        if path.is_absolute():
            return path.as_uri()
        return 'file:' + urllib.parse.quote(path.as_posix(), safe=':/')

    
    try:
        check_db_exist = sqlite3.connect(_path_to_uri(PATH_DB)+'?mode=rw', uri=True)
        print('db connected')
        check_db_exist.close()
    except sqlite3.OperationalError:
        create_db()

    if 'connection' not in g:
        print("connected")
        g.connection = sqlite3.connect(PATH_DB, check_same_thread=False,
        detect_types=sqlite3.PARSE_DECLTYPES)
        g.connection.row_factory = sqlite3.Row

    return g.connection


def close_db(e=None):
    connection = g.pop('connection', None)

    if connection is not None:
        connection.close()


def init_app(app):
    get_db()
    app.teardown_appcontext(close_db)