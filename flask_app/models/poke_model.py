from flask_app.models import user_model
import re
from flask import flash
from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from random import randint
EMAIL_REGEX = re.compile(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+')


def randInt():
    arr = []
    for i in range(3):
        temp = randint(1, 905)
        arr.append(temp)
    return arr


class Pokemon:
    def __init__(self, data):
        self.id = data['id']
        self.price = data['price']
        self.is_shiny = data['is_shiny']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
