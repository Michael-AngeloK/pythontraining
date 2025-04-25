from datetime import datetime
from pydantic import BaseModel, ValidationError
from typing import Optional

class Reservation(BaseModel):
    customer_name: str
    reservation_date: datetime
    number_of_guests: int
    special_request: Optional[str] = None

def create_reservation(data):
    try:
        res = Reservation(**data)
        print(f"Reservation created successfully: name {res.customer_name}, date: {res.reservation_date}, number_of_guests: {res.number_of_guests}")
        if res.special_request:
            print(f"Special Requests: {res.special_request}")
    except ValidationError as e:
        print(f"Failed to create reservation: {e}")

correct_data = {
    "customer_name": "adam",
    "reservation_date": datetime(2025, 12, 31),
    "number_of_guests": 2,
    "special_request": "Extra chair"
}

create_reservation(correct_data)

incorrect_data = {
    "customer_name": "Chen Chu",
    "number_of_guests": 3
}

create_reservation(incorrect_data)