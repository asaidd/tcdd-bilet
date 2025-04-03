from model import Station
import requests
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
STATIONS_URL = "https://cdn-api-prod-ytp.tcddtasimacilik.gov.tr/datas/stations.json?environment=dev&userId=1"

def get_stations() -> dict[str, Station]:
    stations = {}
    try:
        response = requests.get(STATIONS_URL)
        if response.status_code == 200:
            stations_data = response.json()
            for station_data in stations_data:  # Assuming `data` is the JSON list from the API response
                try:
                    station = Station(**station_data)
                    stations[station.name] = station
                except Exception as e:
                    print(f"Failed to parse station data: {station_data}. Error: {e}")

            logger.info(f"Got stations successfully")
        else:
            logger.warning(f"Could not get stations reason: {response.status_code}")
    except Exception as e:
        logger.error(f"Could not get stations reason: {e}")
    finally:
        return stations