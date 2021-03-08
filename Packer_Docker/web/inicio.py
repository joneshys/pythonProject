#!/bin/python3
from flask import Flask, request, redirect, render_template
from flask_mysqldb import MySQL
from os import environ

app = Flask(__name__)

app.config['MYSQL_HOST'] = environ.get('DB_HOST_NAME')
app.config['MYSQL_USER'] = environ.get('DB_USER_NAME')
app.config['MYSQL_PASSWORD'] = environ.get('DB_PASSWD_USERNAME')
app.config['MYSQL_DB'] = environ.get('NAME_DB')
app.config['MYSQL_PORT'] = 58963

mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    return "Hola mundo"

@app.route('/query')
def query():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM test111')
    data = cur.fetchall()
    print(data)
    return render_template('query.html', contacts = data)

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')