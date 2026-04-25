import allure
import requests
import jsonschema
from .schemas.pet_schema import PET_SCHEMA

BASE_URL = "http://5.181.109.28:9090/api/v3"


@allure.feature("Store")
class TestStore:

    @allure.title("Попытка получить информацию о несуществующем заказе")
    def test_get_store_by_order(self):
        with allure.step("Отправка запроса на получение информации о несуществующем заказе"):
            response = requests.get(url = f"{BASE_URL}/store/order/9999")
            print(" ")


        with allure.step("Проврека статуса ответа"):
            assert response.status_code == 404, "Код ответа не совпал с ожидаемым"

        with allure.step("Проверка текстового содержимого"):
            assert response.text == "Order not found", "Текстовое содержимое не совпал с ожидаемым"


    @allure.title("Попытка получения инвентаря магазина")
    def test_get_store_by_inventory(self):
        with allure.step("Отправка звпроса на получение инвентаря магазина"):
            response = requests.get(url = f"{BASE_URL}/store/inventory")

        with allure.step("Проверка статус кода"):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"

        with allure.step("Проверка текстового содержимого"):
            assert response.text == '{"approved":57,"delivered":50}'


    @allure.title("Попытка создания заказа")
    def test_post_store_order(self):
        with allure.step("Подготовка данных для создания нового заказа"):
            payload = {
                "id": 10,
                "petId": 198772,
                "quantity": 7,
                "shipDate": "2026-04-25T01:55:07.615Z",
                "status": "approved",
                "complete": "true"
            }

        with allure.step("Отправка запроса на создание заказа"):
            response = requests.post(url = f"{BASE_URL}/store/order", json = payload)
            print(" ")

        with allure.step("Проверка статус кода"):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"

        with allure.step("Проверка текста ответа"):
            assert response.text == '{"id":10,"petId":198772,"quantity":7,"shipDate":"2026-04-25T01:55:07.615+00:00","status":"approved","complete":true}', "Текст ответа не совпал с ожидаемым"
