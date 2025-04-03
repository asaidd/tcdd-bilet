import logging
from sorgu import query_tickets
from stations import get_stations


logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def main():
    stations = get_stations()

    arrival_station_name = "İSTANBUL(BOSTANCI)"
    departure_station_name = "SELÇUKLU YHT (KONYA)"
    arrival_station_id = stations[arrival_station_name].id
    departure_station_id = stations[departure_station_name].id
    query_response = query_tickets(
        arrival_station_id=arrival_station_id,
        arrival_station_name=arrival_station_name,
        departure_date="08-04-2025 21:00:00",
        departure_station_id=departure_station_id,
        departure_station_name=departure_station_name
    )

    for train in query_response:
        print(f"Departure time: {train.departure_time}, economy: {train.available_economy_seat}, "
                    f"business: {train.available_business_seat},  loca: {train.available_loca_seat}")


main()