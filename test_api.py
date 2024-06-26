import requests
from requests import get

import allure

@allure.title('success requests')
@allure.description('check Facts')
def test_success():
    param = {'animal_type': 'cat', 'amount': '1'}
    url = 'https://cat-fact.herokuapp.com/facts'

    response = requests.get(url, params=param)

    assert response.content is not None
    assert response.status_code == 200 

@allure.title('change animal_type')
@allure.description('change animal_type, it should retern status_code 200')
def test_fail():
    param = {'animal_type': "####", 'amount': '1'}
    url = 'https://cat-fact.herokuapp.com/facts'

    response = requests.get(url, params=param)

    assert response.content is not None
    assert response.status_code == 200

@allure.title('change amount')
@allure.description('change amount, it should retern status_code 200')
def test_fail_1():
    param = {'animal_type': 'cat', 'amount': '0'}
    url = 'https://cat-fact.herokuapp.com/facts'

    response = requests.get(url, params=param)

    assert response.content is not None
    assert response.status_code == 200
