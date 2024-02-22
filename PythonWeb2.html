from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static')

# Dummy user data (replace this with a database in a real application)
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def show_signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    if username in users:
        return "Username already exists. Please choose another one."
    else:
        users[username] = password
        return f"Account created for {username}. You can now <a href='/login'>log in</a>."

@app.route('/login')
def show_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return f"Welcome back, {username}!"
    else:
        return "Invalid username or password. Please try again."

if __name__ == '__main__':
    app.run(debug=True)