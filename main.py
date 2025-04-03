from time import sleep

import telegram
import asyncio
from stations import get_stations
from sorgu import query_tickets

bot = telegram.Bot(token='')
chat_id = ""

async def send_message(text):
    await bot.send_message(chat_id=chat_id, text=text)


async def main():
    while True:
        stations = get_stations()

        arrival_station_name = "İSTANBUL(BOSTANCI)"
        departure_station_name = "SELÇUKLU YHT (KONYA)"
        departure_date = "05-04-2025 21:00:00"

        trains = query_tickets(
            arrival_station_id=stations[arrival_station_name].id,
            arrival_station_name=arrival_station_name,
            departure_date=departure_date,
            departure_station_id=stations[departure_station_name].id,
            departure_station_name=departure_station_name,
            auth="",
        )

        for train in trains:
            if train.available_economy_seat > 0:
                msg = f"{train.available_economy_seat}Economy ticket available for {train.departure_time} at {departure_station_name}-{arrival_station_name}"
                await bot.send_message(chat_id=chat_id, text=msg)
            if train.available_business_seat > 0:
                msg = f"{train.available_business_seat} Business ticket available for {train.departure_time} at {departure_station_name}-{arrival_station_name}"
                await bot.send_message(chat_id=chat_id, text=msg)
            if train.available_loca_seat > 0:
                msg = f"{train.available_loca_seat} LOCA ticket available for {train.departure_time} at {departure_station_name}-{arrival_station_name}"
                await bot.send_message(chat_id=chat_id, text=msg)
            if train.available_business_seat == 0 and train.available_economy_seat == 0 and train.available_loca_seat == 0:
                msg = f"No tickets available for {train.departure_time} at {departure_station_name}-{arrival_station_name}"
                await bot.send_message(chat_id=chat_id, text=msg)
        sleep(300)


if __name__ == "__main__":
    asyncio.run(main())