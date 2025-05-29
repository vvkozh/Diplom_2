class UserData:
    USER_EMAIL = 'test_email@burger.ru'
    USER_PASSWORD = '123456789'
    USER_NAME = 'Vladimir'

class UserDataForChange:
    USER_EMAIL = 'test_change_email@burger.ru'
    USER_PASSWORD = '123456789'
    USER_NAME = 'Vladimir'

class Ingredients:
    INVALID_HASH = ['61c0c5a71d1f82001bdaaa6', '16c0c5a71d1f82001bdaaa61']


class ResponseData:
    RESPONSE_CREATE_EXISTING_USER = {'success': False,
                                     'message': 'User already exists'}
    RESPONSE_CREATE_USER_MISSING_FIELD = {'success': False,
                                          'message': 'Email, password and name are required fields'}
    RESPONSE_INVALID_LOGIN = {'success': False,
                              'message': 'email or password are incorrect'}
    RESPONSE_ERROR_CHANGE_USER_DATA = {'success': False,
                                       'message': 'You should be authorised'}
    RESPONSE_ERROR_CHANGE_EMAIL = {'success': False,
                                   'message': 'User with such email already exists'}
    RESPONSE_INVALID_CREATE_ORDER = {'success': False,
                                    'message': 'Ingredient ids must be provided'}
    RESPONSE_ERROR_GET_ORDERS = {'success': False,
                                 'message': 'You should be authorised'}
