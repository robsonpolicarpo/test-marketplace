import json

import requests

from tests.web.test_data.faker_data import FakerData

BASE_URL_API = 'https://restful-booker.herokuapp.com'


def test_login():
    url_login = '/auth'
    user = 'admin'
    password = 'password123'
    payload = {
        "username": user,
        "password": password
    }
    response = requests.post(BASE_URL_API + url_login, data=payload)
    assert response.status_code == 200
    token = response.json()
    assert token is not None
    return token


def test_search(item=7):
    response = requests.get(f'https://restful-booker.herokuapp.com/booking/{item}')
    assert response.status_code == 200
    return response.json()


def test_create():
    headers = {'Content-Type': 'application/json'}
    route_create = '/booking'
    payload = {
        "firstname": "Robson",
        "lastname": "Brown",
        "totalprice": FakerData().faker.random.randint(1, 999),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2021-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(BASE_URL_API + route_create, headers=headers, data=json.dumps(payload))
    assert response.status_code == 200
    id_created = response.json().get('bookingid')
    assert id_created is not None


def test_update():
    token = test_login().get('token')
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Cookie': f"token={token}"}

    route_update = '/booking/7'
    payload = {
        "firstname": "Robson",
        "lastname": "Test",
        "totalprice": FakerData().faker.random.randint(1, 999),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2021-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(BASE_URL_API + route_update, headers=headers, data=json.dumps(payload))
    assert response.status_code == 200
    search = test_search(7)
    assert search == response.json()
