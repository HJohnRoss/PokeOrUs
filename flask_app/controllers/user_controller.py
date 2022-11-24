from flask_app.models import user_model, poke_model  # CHANGE THIS
from flask_bcrypt import Bcrypt
from flask import flash
from flask import render_template, redirect, request, session, jsonify
from flask_app import app
bcrypt = Bcrypt(app)


@app.route('/')
def re():
    randPoke = poke_model.randInt()
    return render_template('home_page.html', randPoke=randPoke)


@app.route('/register')
def main():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template("register.html")


@app.route('/login')
def log():
    return render_template('login.html')


@app.route('/user/create', methods=['POST'])
def create_user():
    if not user_model.User.validate(request.form):
        return redirect('/register')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        **request.form,
        "password": pw_hash
    }
    user_id = user_model.User.save(data)
    user_in_db = user_model.User.get_by_email(data)
    session['first_name'] = user_in_db.first_name
    session['user_id'] = user_id
    return redirect('/')


@app.route('/login/user', methods=['POST'])
def login():
    data = {"email": request.form["email"]}
    user_in_db = user_model.User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", 'login')
        return redirect("/login")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", 'login')
        return redirect('/login')
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    return redirect("/")


@app.route('/logout')
def logout():
    del session['user_id']
    del session['first_name']
    return redirect('/')
