#Валентина Мысик, 21а-когорта - Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_URL,
                         json=body)


def check_order_information(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_BY_ORDER_URL,
                         params= {"t": track_number})





