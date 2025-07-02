import allure
import requests
import pytest
import data
import generators
from curls import Curls

class TestLogin:
    @allure.title('Тест авторизации пользователя')
    def test_login_user(self):
        payload = {'email': data.UserData.USER_EMAIL,
                   'password': data.UserData.USER_PASSWORD}
        with allure.step('Авторизация пользователя'):
            response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_LOGIN}', data = payload)
        assert response.status_code == 200
        assert response.json()['success'] == True
        assert response.json()['user'] == {'email': data.UserData.USER_EMAIL,
                                           'name': data.UserData.USER_NAME}

    @allure.title('Тест авторизации с неверными данными')
    @pytest.mark.parametrize('email, password, invalid_data', [['correct_email', generators.generate_email(), 'password'],
                                                               [generators.generate_password(), 'correct_password', 'email']])
    def test_login_invalid_data(self, email, password, invalid_data):
        payload = {'email': email if email != 'correct_email' else data.UserData.USER_EMAIL,
                   'password': password if password != 'correct_password' else data.UserData.USER_PASSWORD}
        with allure.step(f'Авторизация с неверным {invalid_data}'):
            response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_LOGIN}', data = payload)
        assert response.status_code == 401
        assert response.json() == data.ResponseData.RESPONSE_INVALID_LOGIN

