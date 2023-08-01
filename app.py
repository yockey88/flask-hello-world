from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect('postgres://lab_10_postgre_user:yEHgdwGoczjfLI3JdgzAt0YSGN0zHha8@dpg-cj46mhd9aq047cahvoc0-a/lab_10_postgre')
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect('postgres://lab_10_postgre_user:yEHgdwGoczjfLI3JdgzAt0YSGN0zHha8@dpg-cj46mhd9aq047cahvoc0-a/lab_10_postgre')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
            First VARCHAR(255) , 
            Last VARCHAR(255) , 
            City VARCHAR(255) , 
            Name VARCHAR(255) , 
            Number INT
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

# @app.route('/db_insert')
# def inserting():
#     conn = psycopg2.connect('postgres://lab_10_postgre_user:yEHgdwGoczjfLI3JdgzAt0YSGN0zHha8@dpg-cj46mhd9aq047cahvoc0-a/lab_10_postgre')
#     cur = conn.cursor()
#     cur.execute('''
#         INSERT INTO Basketball (First , Last , City , Name , Number)
#         VALUES
#             ('Jayson' , 'Taytum' , 'Boston' , 'Celtics' , 0) ,
#             ('Stephen' , 'Curry' , 'San Francisco' , 'Warriors' , 30) ,
#             ('Jayson' , 'Taytum' , 'Denver' , 'Nuggets' , 15) ,
#             ('Jayson' , 'Taytum' , 'Boston' , 'Celtics' , 0);
#     ''')
#     conn.commit()
#     conn.close()
#     return "Basketball Table Successfully Created"