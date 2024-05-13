from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with app.open_resource('schema.sql', mode='r') as f:
        conn.cursor().executescript(f.read())
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/first_name')
def index_first_name():
    conn = get_db_connection()
    users = conn.execute('SELECT first_name FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/age')
def index_age():
    conn = get_db_connection()
    users = conn.execute('SELECT age FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/last_name')
def index_last_name():
    conn = get_db_connection()
    users = conn.execute('SELECT last_name FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/phone')
def index_phone():
    conn = get_db_connection()
    users = conn.execute('SELECT phone FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
