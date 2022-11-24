import stripe
from flask_app.models import user_model
import re
from flask import flash
from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
EMAIL_REGEX = re.compile(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+')
stripe.api_key = 'sk_test_51M4YVwJr2Cg1Gwns3z1yJgmS9jVPhk3mVSxaC1rwQUZbin2Rn63Kt6PUD6IjFRzu60MMZH66Oh23jC8g3UfvqpgR008XDXYTv7'


def products():
    products = stripe.Product.list()
    all_prices = stripe.Price.list()
    products.price = all_prices['data']
    return products
