from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'super_secret_key'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username.upper() == 'KHUSHI' and password.upper() == 'ADMIN':
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('summary_dashboard'))
        else:
            error = 'Invalid username or password!'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# Summary Dashboard After Login
@app.route('/home')
def summary_dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM books")
    total_books = cursor.fetchone()[0]

    conn.close()

    return render_template('summary_dashboard.html', username=session['username'], total_books=total_books)

# Full Book Management
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST' and 'add' in request.form:
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        copies = request.form['copies']
        cursor.execute("INSERT INTO books (title, author, genre, available_copies) VALUES (?, ?, ?, ?)",
                       (title, author, genre, copies))
        conn.commit()

    if request.method == 'POST' and 'delete' in request.form:
        book_id = request.form['book_id']
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()

    search = request.args.get('q')
    if search:
        cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR genre LIKE ?",
                       (f"%{search}%", f"%{search}%", f"%{search}%"))
    else:
        cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM books")
    total_books = cursor.fetchone()[0]

    conn.close()
    return render_template('dashboard.html', books=books, total_books=total_books, search=search)

if __name__ == '__main__':
    app.run(debug=True)



