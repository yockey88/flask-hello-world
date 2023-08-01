from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    # conn.psycopg2.connect('postgres://lab_10_postgre_user:yEHgdwGoczjfLI3JdgzAt0YSGN0zHha8@dpg-cj46mhd9aq047cahvoc0-a/lab_10_postgre')
    # conn.close()
    return "Yo wtf"