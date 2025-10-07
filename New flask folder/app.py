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

DATABASE = {
    'arjun@xyz.com': {'name': 'Arjun', 'password': '123'},
    'test@xyz.com': {'name': 'test', 'password': '123'},}

@app.route('/', methods=['get','post'])
def home():
    user_name = session.get('user_name')
    return render_template("index.html", user_name=session.get('user_name'))

@app.route('/logout')
def logout():
    # Remove the user_name key from the session if it exists
    session.pop('user_name', None)
    session.pop('cart', None) # Clear the cart on logout
    return redirect(url_for('home'))

@app.route('/loginpage', methods=['GET',"POST"] )
def loginpage():
    if request.method == "GET":
        return render_template("loginpage.html")
        
    # If a POST request (form submitted)
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = DATABASE.get(email)
        
        # Check if user exists AND if the password matches
        if user and user['password'] == password:
            session['user_name'] = user['name']
            return redirect(url_for('home')) 
        else:
            # FAILURE: Set the error message and re-render the login page
            error_message = "Invalid email or password. Please try again."
            return render_template("loginpage.html", error=error_message)

@app.route('/signup', methods=['GET',"POST"] )
def signinpage():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get("password")
        confirm_password = request.form.get('confirm_password')
        if email in DATABASE:
             error_message = "Error: Email already registered."
             return render_template("signup.html", error=error_message)

        if password != confirm_password:
            error_message = "Error: Passwords do not match. Please try again."
            return render_template("signup.html", error=error_message)
        
        # SUCCESS: Store user in plain text (for this test)
        DATABASE[email] = {'name': name, 'password': password}
        
        # Log the user in and redirect (PRG pattern)
        session['user_name'] = name
        return redirect(url_for('home')) 
        
    return render_template("signup.html")

@app.route('/menu')
def menu():
    user_name =session.get('user_name')
    cart = session.get('cart', [])
    return render_template('menu.html', menu_items=MENU_ITEMS, cart=cart, user_name=user_name)

@app.route('/add_to_cart/<int:item_id>')
def add_to_cart(item_id):
    cart = session.get('cart', [])
    item = MENU_ITEMS.get(item_id)
    if item:
        cart.append(item)
    session['cart'] = cart
    return redirect(url_for('menu'))


@app.route('/checkout')
def checkout():
    session.pop('cart', None)
    return redirect(url_for('address'))

@app.route('/address')
def address():
    # This route now renders the new thank you template
    return render_template("checkout.html")


if __name__ == '__main__':
    app.run(debug=True)