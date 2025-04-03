from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class CabinClass(BaseModel):
    name: str

    class Config:
        extra = "ignore"

class Segment(BaseModel):
    departureTime: int

    class Config:
        extra = "ignore"

class CabinClassAvailability(BaseModel):
    cabinClass: CabinClass
    availabilityCount: int

    class Config:
        extra = "ignore"


class TrainModel(BaseModel):
    cabinClassAvailabilities: List[CabinClassAvailability]
    segments: List[Segment]

    class Config:
        extra = "ignore"

    @property
    def departure_time(self) -> Optional[str]:
        if self.segments:
            departure_time_epoch = self.segments[0].departureTime / 1000.0
            departure_time = datetime.fromtimestamp(departure_time_epoch)
            return departure_time.__str__()
        return None

    @property
    def available_economy_seat(self) -> Optional[int]:
        for availability in self.cabinClassAvailabilities:
            if availability.cabinClass.name == "EKONOMİ":
                return availability.availabilityCount
        return 0

    @property
    def available_business_seat(self) -> Optional[int]:
        for availability in self.cabinClassAvailabilities:
            if availability.cabinClass.name == "BUSİNESS":
                return availability.availabilityCount
        return 0

    @property
    def available_loca_seat(self) -> Optional[int]:
        for availability in self.cabinClassAvailabilities:
            if availability.cabinClass.name == "LOCA":
                return availability.availabilityCount
        return 0

class Station(BaseModel):
    name: str
    stationNumber: str
    unitId: int
    id: int
    active: bool

    class Config:
        extra = "ignore"
