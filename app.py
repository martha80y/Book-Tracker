from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data storage
books = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        status = request.form['status']
        books.append({'title': title, 'author': author, 'status': status})
        return redirect(url_for('view_books'))
    return render_template('add.html')

@app.route('/books')
def view_books():
    return render_template('books.html', books=books)

@app.route('/delete/<int:index>')
def delete_book(index):
    if 0 <= index < len(books):
        books.pop(index)
    return redirect(url_for('view_books'))

if __name__ == '__main__':
    app.run(debug=True)
