import requests
from typing import List

from model import TrainModel



def query_tickets(departure_station_id, departure_station_name, arrival_station_id, arrival_station_name,
                      departure_date, auth) -> List[TrainModel]:

    # URL for the API endpoint
    url = "https://web-api-prod-ytp.tcddtasimacilik.gov.tr/tms/train/train-availability?environment=dev&userId=1"

    # Headers
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "tr",
        "Authorization": auth,
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://ebilet.tcddtasimacilik.gov.tr",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "unit-id": str(3895)
    }

    # Request payload (body)
    payload = {
        "searchRoutes": [
            {
                "departureStationId": departure_station_id,
                "departureStationName": departure_station_name,
                "arrivalStationId": arrival_station_id,
                "arrivalStationName": arrival_station_name,
                "departureDate": departure_date
            }
        ],
        "passengerTypeCounts": [
            {
                "id": 0,
                "count": 1
            }
        ],
        "searchReservation": False
    }

    # Make the POST request
    trains = []
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        availability_list = data["trainLegs"][0]["trainAvailabilities"]
        for availability in availability_list:
            train_data = availability['trains'][0]
            train = TrainModel(**train_data)
            trains.append(train)

    return trains
