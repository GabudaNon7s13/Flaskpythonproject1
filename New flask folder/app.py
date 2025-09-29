from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/menu')
def menu():
    return render_template("menu.html")

@app.route('/cart')
def cart():
    return render_template("cart.html")

@app.route('/address')
def address():
    return render_template("address.html")

@app.route('/summary')
def summary():
    return render_template("summary.html")

if __name__ == '__main__':
    app.run(debug=True)