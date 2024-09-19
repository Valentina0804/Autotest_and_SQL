#Валентина Мысик, 21а-когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def positive_assert (track_number):
    response = sender_stand_request.check_order_information(track_number)
    assert response.status_code == 200

def test_check_order_by_recent_track():
    response = sender_stand_request.create_order(data.order_body)

    track = response.json()['track']
    positive_assert (track)

