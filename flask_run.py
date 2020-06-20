from flask import Flask, render_template

from pyodbctest import MSDBconnection

app = Flask(__name__)


nwind = MSDBconnection()
results = nwind.sql_query("SELECT * FROM google_books_1299")
list=[results.fetchone()]


@app.route('/')
@app.route('/home')
def home():
    return render_template("homepage.html",list=list)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/page2')
def page2():
    return render_template("page2.html")

@app.route('/add-book')
def add_book():
    return render_template("add-book.html")


@app.route('/index')
def index():
    return render_template("index.html")


if( __name__ == '__main__'):
    app.run(host='0.0.0.0')