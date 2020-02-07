from flask import abort


def payments_calculations(ask_price, down_payment, payment_sched, amort_period, rate):
    if payment_sched == 'weekly':
        num_payments = amort_period * 52
        adjusted_rate = rate/52
    elif payment_sched == 'biweekly':
        num_payments = amort_period * 26
        adjusted_rate = rate/26
    elif payment_sched == 'monthly':
        num_payments = amort_period * 12
        adjusted_rate = rate/12
    else:
        abort(200)

    temp = down_payment/ask_price
    if 0.05 <= temp < 0.10:
        insurance = 0.0315
    elif 0.10 <= temp < 0.15:
        insurance = 0.024
    elif 0.15 <= temp < 20:
        insurance = 0.018
    elif 20 <= temp:
        insurance = 0.0

    principal = ask_price * (1+insurance)

    returnable = principal*((adjusted_rate*((1+adjusted_rate)**num_payments))/(((1+adjusted_rate)**num_payments)-1))
    return returnable


def valid_down(ask_price, down_payment):
    if ask_price>500000:
        min_down = (0.1*(ask_price-500000))+25000
    else:
        min_down = ask_price*0.05

    if down_payment>=min_down:
        return True
    else:
        return False


def principle_finder(payment_amount, schedule, period, rate):
    if schedule == 'weekly':
        num_payments = period * 52
        adjusted_rate = rate/52
    elif schedule == 'biweekly':
        num_payments = period * 26
        adjusted_rate = rate/26
    elif schedule == 'monthly':
        num_payments = period * 12
        adjusted_rate = rate/12
    else:
        abort(200)
    x = payment_amount * ((((1 + adjusted_rate)**num_payments) - 1)/(adjusted_rate * (1 + adjusted_rate) ** num_payments))
    print((adjusted_rate**num_payments))
    return x
