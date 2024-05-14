from flask import Flask, render_template, request, redirect
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

# Todos los datos
@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

# Datos por edad
@app.route('/age')
def index_age():
    conn = get_db_connection()
    users = conn.execute('SELECT age FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

# Datos por nombre
@app.route('/first_name')
def index_first_name():
    conn = get_db_connection()
    users = conn.execute('SELECT first_name FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

# Datos por apellido
@app.route('/last_name')
def index_last_name():
    conn = get_db_connection()
    users = conn.execute('SELECT last_name FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

# Datos por número de teléfono
@app.route('/phone')
def index_phone():
    conn = get_db_connection()
    users = conn.execute('SELECT phone FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

# Añadir usuario
@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        phone = request.form['phone']
        conn = get_db_connection()
        conn.execute('INSERT INTO users (first_name, last_name, age, phone) VALUES (?, ?, ?, ?)',
                     (first_name, last_name, age, phone))
        conn.commit()
        conn.close()
    return redirect('/')

# Borrar usuario por id
@app.route('/delete_user/<int:id>', methods=['POST'])
def delete_user(id):
    if request.method == 'POST':
        conn = get_db_connection()
        conn.execute('DELETE FROM users WHERE id = ?', (id,))
        conn.commit()
        conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)