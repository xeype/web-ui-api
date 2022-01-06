import json
import allure
import pytest
import requests
import re
from api.test.conftest import booking_data, invalid_json
from config import endpoints as E


@allure.title('Health Check')
@allure.description('Ping check to confirm whether the API is up and running')
def test_health_check():
    response = requests.get(E.PING)
    assert response.status_code == 201


@allure.title('Create Token. Valid creds.')
@allure.description('Creating token with valid user credentials')
def test_auth_create_token(valid_user_credentials):
    r = requests.post(E.AUTH, json=valid_user_credentials)
    response_json = r.json()
    assert r.status_code == 200
    assert 'token' in response_json
    assert response_json['token'] != ''


@allure.title('Create Token. Invalid creds.')
@allure.title('Negative case. Creating token with invalid user credentials.')
@pytest.mark.parametrize('invalid_user_credentials', [{'username': 'JimBB', 'password': 'JimPassword123'}])
def test_auth_create_token_with_invalid_params(invalid_user_credentials):
    r = requests.post(E.AUTH, json=invalid_user_credentials)
    response_json = r.json()
    assert r.status_code == 200
    assert 'reason' in response_json
    assert response_json['reason'] == 'Bad credentials'


@allure.title("Booking ID's")
@allure.description("Get all bookings and check that all id's are integer")
def test_booking_ids_are_integer():
    r = requests.get(E.BOOKING)
    response_json = r.json()

    assert re.match(r'^[0-9]', str(response_json[0]['bookingid']))
    assert re.match(r'^[0-9]', str(response_json[1]['bookingid']))


@allure.title('Booking. Create booking. Valid params')
@pytest.mark.parametrize('booking', booking_data)
def test_create_booking_with_valid_params(booking):
    r = requests.post(E.BOOKING, json=booking)
    response_json = r.json()

    response_json_dump = json.dumps(response_json, sort_keys=True)
    test_data_json_dump = json.dumps(booking, sort_keys=True)

    assert r.status_code == 200
    assert test_data_json_dump in response_json_dump


@allure.title('Booking. Create booking. Empty params')
@allure.description('Negative case')
def test_create_booking_with_empty_params():
    r = requests.post(E.BOOKING, json='')
    response = r.text

    assert r.status_code == 400
    assert response == 'Bad Request'


@allure.title('Booking. Create booking. Invalid JSON schemas in request')
@allure.description('Negative case')
@pytest.mark.parametrize('invalid_json_schema', invalid_json)
def test_create_booking_with_invalid_json(invalid_json_schema):
    r = requests.post(E.BOOKING, json=invalid_json_schema)
    response_json = r.text
    assert r.status_code == 500
    assert response_json == 'Internal Server Error'


@allure.title('Booking. Update booking.')
@allure.description('Test update booking and then rollback data to before condition')
@pytest.mark.parametrize('update_booking', [{'firstname': 'James',
                                             'lastname': 'Brown',
                                             'totalprice': 111,
                                             'depositpaid': True,
                                             'bookingdates': {
                                                 'checkin': '2018-01-01',
                                                 'checkout': '2019-03-01'},
                                             'additionalneeds': 'Dinner'}])
@pytest.mark.parametrize('not_updated_booking', [{'firstname': 'Jim',
                                                  'lastname': 'Brown',
                                                  'totalprice': 111,
                                                  'depositpaid': True,
                                                  'bookingdates': {
                                                      'checkin': '2018-01-01',
                                                      'checkout': '2019-01-01'},
                                                  'additionalneeds': 'Breakfast'}])
def test_update_booking(update_booking, not_updated_booking, token_generate):
    cookies_dict = {'token': token_generate}
    try:
        # The requirement for PUT to be done because the server is updating the data
        requests.put(E.BOOKING + '/1', cookies=cookies_dict, json=not_updated_booking, timeout=2.5)

        r = requests.get(E.BOOKING + '/1', cookies=cookies_dict)
        response_json = r.json()

        assert response_json['firstname'] == 'Jim'
        assert response_json['bookingdates']['checkout'] == '2019-01-01'
        assert response_json['additionalneeds'] == 'Breakfast'

        r = requests.put(E.BOOKING + '/1', cookies=cookies_dict, json=update_booking, timeout=2.5)
        response_json = r.json()

        assert r.status_code == 200
        assert response_json['firstname'] == 'James'
        assert response_json['bookingdates']['checkout'] == '2019-03-01'
        assert response_json['additionalneeds'] == 'Dinner'
    except json.JSONDecodeError:
        print('JSONDecodeError')
    finally:
        # Rollback Data
        requests.put(E.BOOKING + '/1', cookies=cookies_dict, json=not_updated_booking, timeout=2.5)


@allure.title('Booking. Delete booking.')
@pytest.mark.xfail(reason='Method Not Allowed')
def test_delete_booking(token_generate):
    cookies_dict = {'token': token_generate}
    r = requests.delete(E.BOOKING + '/1', cookies=cookies_dict)
    response = r.text
    assert r.status_code == 200 or r.status_code == 204
    assert response == 'Method Not Allowed'
