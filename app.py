from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/delete/<int:user_id>', methods=["POST"])
def delete_user(user_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update/<int:user_id>', methods=['GET'])
def get_update_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    if user is None:
        return "User not found", 404
    return render_template('update.html', user=user)

@app.route('/update/<int:user_id>', methods=['POST'])
def post_update_user(user_id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    phone = request.form['phone']
    
    conn = get_db_connection()
    conn.execute('UPDATE users SET first_name = ?, last_name = ?, age = ?, phone = ? WHERE id = ?',
                 (first_name, last_name, age, phone, user_id))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)