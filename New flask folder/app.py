from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/loginpage', methods=['GET',"POST"] )
def loginpage():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        return render_template("/")
    return render_template("loginpage.html")

@app.route('/signuppage', methods=['GET',"POST"] )
def signinpage():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get("password")
        confirm_password = request.form.get('confirm_password')
        if confirm_password == password:
            return "Signup successful! Redirecting you now..."
            
        else:
            error_message = "Error: Passwords do not match. Please try again."
            return render_template("signuppage.html", error=error_message)
        return render_template("/")
    return render_template("signuppage.html")

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