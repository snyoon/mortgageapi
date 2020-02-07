from api import app
from flask import json
import pytest


# testing correct result for payment amount
def test_payment_amount():
    response = app.test_client().get(
        '/payment-amount?askingprice=750000&downpayment=50000&schedule=monthly&period=5'
    )
    result = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert result["paymentamount"] == 13729.80262203904


# testing correct result for mortgage amount
def test_mortgage_amount():
    response = app.test_client().get(
        '/mortgage-amount?paymentamount=14073&schedule=monthly&period=5'
    )
    result = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert result["maxprinciple"] == 792962.9379758061


# testing invalid down payment query
def test_payment_amount_invalid_down_payment():
    response = app.test_client().get(
        '/payment-amount?askingprice=750000&downpayment=500&schedule=monthly&period=5'
    )
    assert response.status_code == 400


# testing invalid schedule query
def test_payment_amount_invalid_schedule():
    response = app.test_client().get(
        '/payment-amount?askingprice=750000&downpayment=500&schedule=123&period=5'
    )
    assert response.status_code == 400


# testing invalid period inquiry
def test_payment_amount_invalid_period():
    response = app.test_client().get(
        '/payment-amount?askingprice=750000&downpayment=500&schedule=monthly&period=100'
    )
    assert response.status_code == 400


# testing for session change when interest rate is patched
def test_interest_rate():
    response = app.test_client().patch(
        '/interest-rate',
        json={'Interest Rate': '5.0'})
    result = json.loads(response.data)
    assert response.status_code == 200
    assert result["newrate"] == '5.0'
