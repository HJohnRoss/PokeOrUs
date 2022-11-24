from flask_app.models import user_model, poke_model, likes_model  # CHANGE THIS
from flask_bcrypt import Bcrypt
from flask import flash
from flask import render_template, redirect, request, session, jsonify
from flask_app import app
bcrypt = Bcrypt(app)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/connect')
def connect():
    all_likes = user_model.User.all_liked_poke()
    return render_template('likes_dashboard.html', all_likes=all_likes)


@app.route('/poke/search')
def one_store():
    return render_template('search.html')


@app.route('/poke/show/<int:id>')
def show(id):
    all_users = user_model.User.get_by_id({'id': session['user_id']})
    return render_template('show_poke.html', id=id, all_users=all_users)


@app.route('/api/fav/<int:id>')
def add_fav(id):
    data = {
        'id': id,
        'user_id': session['user_id']
    }
    likes_model.Like.add_like(data)
    return redirect(f'/poke/show/{id}')


@app.route('/api/fav/delete/<int:id>')
def delete_fav(id):
    data = {
        'id': id,
        'user_id': session['user_id']
    }
    likes_model.Like.delete_like(data)
    return redirect(f'/poke/show/{id}')


@app.route('/favorites/<int:id>')
def show_one(id):
    all_likes = user_model.User.one_users_liked_poke({'id': id})
    return render_template('favorites.html', all_likes=all_likes)
