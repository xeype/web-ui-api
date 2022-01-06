import pytest
import requests
from config import endpoints as E


@pytest.fixture()
def token_generate(valid_user_credentials):
    r = requests.post(E.AUTH, json=valid_user_credentials)
    response_json = r.json()
    token = response_json['token']
    return token


@pytest.fixture()
def valid_user_credentials():
    return {'username': 'admin', 'password': 'password123'}


booking_data = [{'firstname': 'Jim',
                 'lastname': 'Brown',
                 'totalprice': 111,
                 'depositpaid': True,
                 'bookingdates': {
                     'checkin': '2018-01-01',
                     'checkout': '2019-01-01'}},
                {'firstname': 'Helen',
                 'lastname': 'Crow',
                 'totalprice': 1230,
                 'depositpaid': False,
                 'bookingdates': {
                     'checkin': '2022-04-24',
                     'checkout': '2022-05-24'}},
                {'firstname': 'Ginger',
                 'lastname': 'Slipknot',
                 'totalprice': 130,
                 'depositpaid': False,
                 'bookingdates': {
                     'checkin': '2016-04-24',
                     'checkout': '2016-05-24'},
                 'additionalneeds': 'Breakfast'}
                ]


@pytest.fixture(params=booking_data)
def booking(request):
    return request.param


invalid_json = [{'totalprice': 111,
                 'depositpaid': True,
                 'bookingdates': {
                     'checkin': '2018-01-01',
                     'checkout': '2019-01-01'}},
                {'firstname': 'Ginger',
                 'lastname': 'Slipknot',
                 'totalprice': 130,
                 'depositpaid': False,
                 },
                {'firstname': 'Ginger',
                 'lastname': 'Slipknot',
                 'bookingdates': {
                     'checkin': '2016-04-24',
                     'checkout': '2016-05-24'}}]


@pytest.fixture(params=invalid_json)
def invalid_json_schema(request):
    return request.param
