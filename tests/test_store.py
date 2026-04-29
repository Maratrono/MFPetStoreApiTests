import allure
import requests
import jsonschema
from .schemas.store_schema import STORE_SCHEMA, inventory_schema

BASE_URL = "http://5.181.109.28:9090/api/v3"


@allure.feature("Store")
class TestStore:

    @allure.title("Попытка получить информацию о несуществующем заказе")
    def test_get_store_by_order(self):
        with allure.step("Отправка запроса на получение информации о несуществующем заказе"):
            response = requests.get(url = f"{BASE_URL}/store/order/9999")


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
            jsonschema.validate(response.json(), inventory_schema)



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


        with allure.step("Проверка статус кода и валидация json схемы"):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"
            jsonschema.validate(response.json(), STORE_SCHEMA)
            response_json = response.json()


        with allure.step("Проверка текста ответа"):
            assert response_json["id"] == payload["id"], "id заказа не совпадает с ожидаемым"
            assert response_json["petId"] == payload["petId"], "petId заказа не совпадает с ожидаемым"
            assert response_json["quantity"] == payload["quantity"], "quantity заказа не совпадает с ожидаемым"
            assert response_json["status"] == payload["status"], "status заказа не совпадает с ожидаемым"


    @allure.title ("Попытка получения информации о заказе по ID")
    def test_get_store_by_id(self, create_order):
        with allure.step("Получение ID созданного заказа"):
            store_id = create_order["id"]

        with allure.step("Отправка get запроса по ID"):
            response = requests.get(url = f"{BASE_URL}/store/order/{store_id}")
            assert response.status_code == 200, "Код ответа не совпадает с ожидаемым"
            assert response.json()["id"] == store_id, "Id запроса не совпадает с ответом"

    @allure.title ("Попытка удалить заказ по ID")
    def test_delete_store_by_id(self, create_order):
        with allure.step("Получение ID созданного заказа"):
            store_id = create_order["id"]

        with allure.step("Удаление заказа по ID"):
            response = requests.delete(url = f"{BASE_URL}/store/order/{store_id}")
            assert response.status_code == 200, "Статус ответа не совпадает с ожидаемым"

        with allure.step("Отправка get запроса для проверки удаления"):
            response = requests.get(f"{BASE_URL}/store/order/{store_id}")
            assert response.status_code == 404, "Код ответа не совпал с ожидаемым"

