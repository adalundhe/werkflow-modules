from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerCapacityReservationFilter(BaseModel):
    Name: Literal['Status']
    Values: list[StrictStr]
