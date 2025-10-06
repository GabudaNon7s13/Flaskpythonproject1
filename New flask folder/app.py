from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.secret_key = 'sfjbgk'

MENU_ITEMS = {
    1: {'name': 'Espresso', 'price': 280},
    2: {'name': 'Cappuccino', 'price': 380},
    3: {'name': 'Latte', 'price': 396},
    4: {'name': 'Mocha', 'price': 420},
    5: {'name': 'Cold Brew', 'price': 352},
    6: {'name': 'Red Velvet Cake ', 'price': 550},
    7: {'name': 'Chocolate Cake', 'price': 500},
    8: {'name': 'Pinnapple Cake', 'price': 600},
    9: {'name': 'Strawberry Pastry', 'price': 300},
    10: {'name': 'Vanilla Pastry', 'price': 286},
    11: {'name': 'Butterscotch Pastry', 'price': 256},
    12: {'name': 'Bread', 'price': 120},
    13: {'name': 'Brownie', 'price': 250},
    14: {'name': 'Veg Pizza', 'price': 350},
    15: {'name': 'Pasta', 'price': 350},
    16: {'name': 'Fries', 'price': 150},
    }

@app.route('/', methods=['get','post'])
def home():
    user_name = session.get('user_name')
    return render_template("index.html")

@app.route('/loginpage', methods=['GET',"POST"] )
def loginpage():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        return render_template("/")
    return render_template("loginpage.html")

@app.route('/signup', methods=['GET',"POST"] )
def signinpage():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get("password")
        confirm_password = request.form.get('confirm_password')
        if confirm_password == password:
            return render_template("/")
            
        else:
            error_message = "Error: Passwords do not match. Please try again."
            return render_template("signup.html", error=error_message)
        
    return render_template("signup.html")

@app.route('/menu')
def menu():
    cart = session.get('cart', [])
    return render_template('menu.html', menu_items=MENU_ITEMS, cart=cart)

@app.route('/add_to_cart/<int:item_id>')
def add_to_cart(item_id):
    cart = session.get('cart', [])
    item = MENU_ITEMS.get(item_id)
    if item:
        cart.append(item)
    session['cart'] = cart
    return redirect(url_for('menu'))

@app.route('/cart')
def cart():
    return render_template("cart.html")

@app.route('/address')
def address():
    return render_template("address.html")


if __name__ == '__main__':
    app.run(debug=True)