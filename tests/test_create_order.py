import allure
import pytest
import requests
import generators
import data
from curls import Curls

class TestCreateOrder:
    @allure.title('Тест создания заказа с авторизацией')
    @pytest.mark.parametrize('size', [1, 3, 5])
    def test_create_order_with_authorization(self, login_user, get_ingredients, size):
        access_token = {'Authorization': login_user['accessToken']}
        payload = {'ingredients': generators.generate_list_ingredients(size, get_ingredients)}
        with allure.step(f'Создание заказа с {size} ингредиентами'):
            response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_CREATE_ORDER}', data = payload, headers=access_token)
        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title('Тест создания заказа без авторизации')
    def test_create_order_without_authorization(self, login_user, get_ingredients):
        payload = {'ingredients': generators.generate_list_ingredients(1, get_ingredients)}
        with allure.step(f'Создание заказа без авторизации'):
            response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_CREATE_ORDER}', data = payload)
        assert response.status_code == 401
        assert response.json()['success'] == False

    @pytest.mark.parametrize('hash_ingredient', data.Ingredients.INVALID_HASH)
    @allure.title('Тест создания заказа с невалидным хэшом ингредиента')
    def test_create_order_with_invalid_hash(self, login_user, hash_ingredient):
        access_token = {'Authorization': login_user['accessToken']}
        payload = {'ingredients': hash_ingredient}
        with allure.step('Создание заказа с невалидным хэшом ингредиента'):
            response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_CREATE_ORDER}', data = payload, headers=access_token)
        assert response.status_code == 500

    @allure.title('Тест создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self, login_user):
        access_token = {'Authorization': login_user['accessToken']}
        payload = {'ingredients': []}
        with allure.step('Создание заказа без ингредиентов'):
            response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_CREATE_ORDER}', data = payload, headers=access_token)
        assert response.status_code == 400
        assert response.json() == data.ResponseData.RESPONSE_INVALID_CREATE_ORDER

