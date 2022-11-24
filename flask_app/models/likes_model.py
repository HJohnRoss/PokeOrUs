from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
from flask_app.models import user_model
EMAIL_REGEX = re.compile(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+')


class Like:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_like(cls, data):
        query = """
        INSERT INTO likes (id, user_id)
        VALUES (%(id)s, %(user_id)s)
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def delete_like(cls, data):
        query = """
        DELETE FROM likes
        WHERE id = %(id)s AND user_id = %(user_id)s
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
