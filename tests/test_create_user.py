import allure
import requests
import pytest
import data
import generators
from curls import Curls

class TestCreateUser:
    @allure.title('Тест создания пользователя')
    def test_create_user(self, generate_data_and_delete_user):
        payload = generate_data_and_delete_user
        with allure.step('Создание пользователя'):
            response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_REGISTRATION}', data = payload)
        assert response.status_code == 200
        assert response.json()['user'] == {'email': payload['email'], 'name': payload['name']}

    @allure.title('Тест создания уже созданного пользователя')
    def test_create_existing_user(self):
        payload = {'email': data.UserData.USER_EMAIL,
                   'password': data.UserData.USER_PASSWORD,
                   'name': data.UserData.USER_NAME}
        with allure.step('Создание уже созданного пользователя'):
            response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_REGISTRATION}', data = payload)
        assert response.status_code == 403
        assert response.json() == data.ResponseData.RESPONSE_CREATE_EXISTING_USER

    @allure.title('Тест создания пользователя без указания одного из полей')
    @pytest.mark.parametrize('missing_field', ['email', 'password', 'name'])
    def test_create_user_with_missing_field(self, missing_field):
        if missing_field == 'email':
            payload = {'password': generators.generate_password(),
                       'name': generators.generate_name()}
        elif missing_field == 'password':
            payload = {'email': generators.generate_email(),
                       'name': generators.generate_name()}
        else:
            payload = {'email': generators.generate_email(),
                       'password': generators.generate_password()}
        with allure.step(f'Создание пользователя {missing_field}'):
            response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_REGISTRATION}', data = payload)
        assert response.status_code == 403
        assert response.json() == data.ResponseData.RESPONSE_CREATE_USER_MISSING_FIELD