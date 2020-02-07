from api import app
from flask import Flask, session, request, make_response, flash, jsonify, abort

from api.helpers import valid_down, payments_calculations, principle_finder


@app.route('/payment-amount', methods=['GET'])
def payment_amount():
    try:
        ask_price = float(request.args.get('askingprice'))
        down_payment = float(request.args.get('downpayment'))
        payment_schedule = request.args.get('schedule')
        amort_period = float(request.args.get('period'))
    except ValueError:
        abort(400)

    # checks the query for validness
    if ask_price < 0 or down_payment < 0 or amort_period < 5 or amort_period > 25:
        abort(400)
    # checks if down payment is enough for the asking price
    if not valid_down(ask_price, down_payment):
        abort(400)
    # finds current active rate for application
    if 'rate' in session:
        rate = session['rate']
    else:
        rate = '2.5'
    rate_percent = float(rate)/100
    return_amount = payments_calculations(ask_price, down_payment, payment_schedule, amort_period, rate_percent)
    return jsonify(paymentamount=return_amount), 200


@app.route('/mortgage-amount', methods=['GET'])
def mortgage_amount():
    try:
        pay_amount = float(request.args.get('paymentamount'))
        payment_schedule = request.args.get('schedule')
        amort_period = float(request.args.get('period'))
    except ValueError:
        abort(400)

    # finds current active rate for application
    if 'rate' in session:
        rate = session['rate']
    else:
        rate = '2.5'
    rate_percent = float(rate) / 100
    principle = principle_finder(pay_amount, payment_schedule, amort_period, rate_percent)
    return jsonify(maxprinciple=principle), 200


@app.route('/interest-rate', methods=['PATCH'])
def interest_rate():
    if not request.get_json() or 'Interest Rate' not in request.get_json():
        abort(400)
    req_body = request.get_json()
    new_rate = req_body['Interest Rate']
    if 'rate' in session:
        old_rate = session['rate']
        session['rate'] = new_rate
        return jsonify(oldrate=old_rate, newrate=new_rate), 200
    else:
        old_rate = '2.5'
        session['rate'] = new_rate
        return jsonify(oldrate=old_rate, newrate=new_rate), 200
