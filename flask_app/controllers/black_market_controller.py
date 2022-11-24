from flask_app.models import user_model, poke_model, likes_model, stipe  # CHANGE THIS
from flask_bcrypt import Bcrypt
from flask import flash
from flask import render_template, redirect, request, session, jsonify
from flask_app import app
import stripe
bcrypt = Bcrypt(app)


@app.route('/black_market')
def show_black_market():
    all_products = stipe.products()
    for price in all_products.price:
        price['unit_amount'] /= 100
        if len(str(price['unit_amount'])) < 4:
            price['unit_amount'] = str(price['unit_amount']) + '0'
        price['unit_amount'] = float(price['unit_amount'])
    return render_template('market_dashboard.html', all_products=all_products)

@app.route('/cancel')
def cancel():
    return render_template('cancel.html')


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': request.form['id'],
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:5000' + '/success',
            cancel_url='http://127.0.0.1:5000' + '/black_market',
        )
    except Exception as e:
        return str(e)
    return redirect(checkout_session.url, code=303)
