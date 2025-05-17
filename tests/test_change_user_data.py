import pytest
import requests
import data
import allure
import generators
from curls import Curls


class TestChangeUserData:
    @allure.title('Тест изменения данных пользователя с авторизацией')
    @pytest.mark.parametrize('change_param, generate_method', [['email', 'generate_email'],
                                                               ['name', 'generate_name']])
    def test_change_user_data_with_login(self, login_and_return_data, change_param, generate_method):
        access_token = login_and_return_data['accessToken']
        generate_param = getattr(generators, generate_method)
        payload = {change_param: generate_param()}
        with allure.step(f'Изменение {change_param} пользователя'):
            response = requests.patch(f'{Curls.MAIN_URL}{Curls.URL_CHANGE_USER_DATA}', data = payload, headers = {'Authorization': access_token})
        assert response.status_code == 200
        assert response.json()['success'] == True
        assert response.json()['user'][f'{change_param}'] == payload[f'{change_param}']

    @allure.title('Тест изменения данных пользователя без авторизации')
    @pytest.mark.parametrize('change_param, generate_method', [['email', 'generate_email'],
                                                               ['name', 'generate_name']])
    def test_change_user_data_without(self, change_param, generate_method):
        generate_param = getattr(generators, generate_method)
        payload = {change_param: generate_param()}
        with allure.step(f'Изменение {change_param} пользователя без авторизации'):
            response = requests.patch(f'{Curls.MAIN_URL}{Curls.URL_CHANGE_USER_DATA}', data = payload)
        assert response.status_code == 401
        assert response.json() == data.ResponseData.RESPONSE_ERROR_CHANGE_USER_DATA

    @allure.title('Тест изменения почты пользователя на уже используемую')
    def test_change_user_email(self, login_and_return_data):
        access_token = login_and_return_data['accessToken']
        payload = {'email': data.UserDataForChange.USER_EMAIL}
        with allure.step(f'Изменение почты пользователя на уже используемую'):
            response = requests.patch(f'{Curls.MAIN_URL}{Curls.URL_CHANGE_USER_DATA}', data = payload, headers = {'Authorization': access_token})
        assert response.status_code == 403
        assert response.json() == data.ResponseData.RESPONSE_ERROR_CHANGE_EMAIL