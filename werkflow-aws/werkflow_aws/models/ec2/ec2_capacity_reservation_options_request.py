from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class EC2CapacityReservationOptionsRequest(BaseModel):
    UsageStrategy: Literal['use-capacity-reservations-first'] | None = None
