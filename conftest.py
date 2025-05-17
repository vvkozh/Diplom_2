import requests
import generators
import data
import pytest
from curls import Curls

@pytest.fixture()
def create_user():
    payload = {'email': generators.generate_email(),
               'password': generators.generate_password(),
               'name': generators.generate_name()}
    response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_REGISTRATION}', data=payload)
    yield response.json()

@pytest.fixture(scope='session')
def login_user():
    payload = {'email': data.UserData.USER_EMAIL,
               'password': data.UserData.USER_PASSWORD}
    response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_LOGIN}', data=payload)
    return response.json()

@pytest.fixture()
def login_and_return_data():
    payload = {'email': data.UserDataForChange.USER_EMAIL,
               'password': data.UserDataForChange.USER_PASSWORD}
    response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_LOGIN}', data=payload)
    yield response.json()
    return_name = {'email': data.UserDataForChange.USER_EMAIL,
                   'name': data.UserDataForChange.USER_NAME}
    requests.patch(f'{Curls.MAIN_URL}{Curls.URL_CHANGE_USER_DATA}', data=return_name,
                          headers={'Authorization': response.json()['accessToken']})

@pytest.fixture(scope='session')
def get_ingredients():
    response = requests.get(f'https://stellarburgers.nomoreparties.site/api/ingredients')
    list_ingredients = []
    for i in range(len(response.json()['data'])):
        list_ingredients.append(response.json()['data'][i]['_id'])
    return list_ingredients
