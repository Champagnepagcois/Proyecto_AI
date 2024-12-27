from flask import g
import psycopg2

def init_db(app):
    @app.teardown_appcontext
    def close_db(exception):
        db = g.pop('db', None)
        if db is not None:
            db.close()

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            dbname="example_db",
            user="postgres",
            password="password",
            host="localhost",
            port=5432
        )
    return g.db
