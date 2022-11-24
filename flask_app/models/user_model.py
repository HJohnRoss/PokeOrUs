from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
from flask_app.models import poke_model, likes_model
EMAIL_REGEX = re.compile(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_by_email(cls, data):
        query = """
        SELECT * FROM users WHERE email = %(email)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def get_by_id(cls, data):
        query = """
        SELECT * FROM users
        LEFT JOIN likes on users.id = user_id
        WHERE users.id = %(id)s
        ORDER BY likes.created_at DESC
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            user = cls(result[0])
            user.likes = []
            print(result)
            if result[0]['likes.id']:
                for row in result:
                    user.likes.append(row['likes.id'])
            return user
        return []

    @classmethod
    def all_liked_poke(cls):
        query = """
        SELECT * FROM users
        JOIN likes ON users.id = likes.user_id
        ORDER BY likes.created_at DESC
        """
        result = connectToMySQL(DATABASE).query_db(query)
        print(result)
        if result:
            pokemons = []
            for row in result:
                users = cls(row)
                data = {
                    **row,
                    'id': row['likes.id'],
                }
                this_poke = likes_model.Like(data)
                users.poke = this_poke
                pokemons.append(users)
            return pokemons
        return []

    @classmethod
    def one_users_liked_poke(cls, data):
        query = """
        SELECT * FROM users
        JOIN likes ON users.id = likes.user_id
        WHERE users.id = %(id)s
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        if result:
            pokemons = []
            for row in result:
                users = cls(row)
                data = {
                    **row,
                    'id': row['likes.id'],
                    'created_at' : row['likes.created_at'],
                    'updated_at' : row['likes.updated_at']
                }
                this_poke = likes_model.Like(data)
                users.poke = this_poke
                pokemons.append(users)
            return pokemons
        return []

    @staticmethod
    def validate(user):
        is_valid = True
        if len(user['first_name']) < 1:
            flash('first name required', 'reg')
            is_valid = False
        elif len(user['first_name']) < 2:
            flash('first name must be 2 characters', 'reg')
            is_valid = False
        if len(user['last_name']) < 1:
            flash('last name required', 'reg')
            is_valid = False
        elif len(user['last_name']) < 2:
            flash('last name must be 2 characters', 'reg')
            is_valid = False
        if len(user['email']) < 1:
            flash('email is required', 'reg')
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']):
            flash('email is invalid', 'reg')
            is_valid = False
        else:
            data = {
                'email': user['email']
            }
            potential_user = User.get_by_email(data)
            if potential_user:
                flash('email taken', 'reg')
                is_valid = False
        if len(user['password']) < 7:
            flash('password must be 8 characters', 'reg')
            is_valid = False
        elif not user['password'] == user['confirm_pw']:
            is_valid = False
            flash('passwords dont match', 'reg')
        return is_valid
